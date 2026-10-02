#!/usr/bin/env python3
"""One bounded, read-only tmux snapshot. No classification, polling or input."""
import datetime
import hashlib
import json
import re
import socket
import subprocess


def run(args):
    result = subprocess.run(['tmux', *args], capture_output=True, text=True,
                            errors='replace', timeout=10, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip()[:1000] or 'tmux read failed')
    return result.stdout.rstrip('\n')


def snapshot(reader=run):
    result = {'computer': socket.gethostname(),
              'observed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'coverage': 'complete', 'panes': [], 'errors': []}
    try:
        result['server'] = reader(['display-message', '-p', '#{pid}'])
        result['socket'] = reader(['display-message', '-p', '#{socket_path}'])
        # Only machine IDs cross a delimiter; user-controlled names are read separately.
        inventory = reader(['list-panes', '-a', '-F',
                            '#{session_id} #{window_id} #{pane_id} #{pane_pid}'])
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
        result.update(coverage='unavailable', errors=[str(exc)])
        return result
    panes = {}
    for row in inventory.splitlines():
        if not re.fullmatch(r'\$\d+ @\d+ %\d+ \d+', row):
            result['coverage'] = 'partial'
            result['errors'].append('Malformed inventory row; not used as a target')
            continue
        session, window, pane, pid = row.split()
        membership = {'session_id': session, 'window_id': window}
        try:
            membership['session_name'] = reader(['display-message', '-p', '-t', session, '#{session_name}'])
            membership['window_name'] = reader(['display-message', '-p', '-t', window, '#{window_name}'])
        except (OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
            result['coverage'] = 'partial'
            membership['error'] = str(exc)
        if pane in panes:
            panes[pane]['memberships'].append(membership)
            continue
        item = {'pane_id': pane, 'pane_pid': int(pid), 'memberships': [membership]}
        panes[pane] = item
        result['panes'].append(item)
        try:
            for key in ('pane_current_command', 'pane_current_path', 'pane_dead'):
                item[key] = reader(['display-message', '-p', '-t', pane, '#{' + key + '}'])
            output = reader(['capture-pane', '-p', '-t', pane, '-S', '-120'])
            # Bound returned content; hash is for change detection, never authorization.
            item['tail'] = output[-24000:]
            item['tail_truncated'] = len(output) > 24000
            item['fingerprint'] = hashlib.sha256(item['tail'].encode()).hexdigest()
            current_pid = reader(['display-message', '-p', '-t', pane, '#{pane_pid}'])
            if current_pid != pid:
                raise RuntimeError('Pane changed during capture; recapture before classification')
        except (OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
            item['error'] = str(exc)
            result['coverage'] = 'partial'
    return result


if __name__ == '__main__':
    print(json.dumps(snapshot(), ensure_ascii=True, indent=2))
