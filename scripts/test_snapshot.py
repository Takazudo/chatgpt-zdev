"""Exercise fresh inventories, linked panes, races and failure coverage without user tmux."""
import importlib.util
import unittest
import shutil
import subprocess
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location('snapshot', Path(__file__).resolve().parents[1] / 'skills/zstatus/scripts/snapshot.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SnapshotTests(unittest.TestCase):
    def reader(self, rows, fail=None, pid='42'):
        self.calls = []
        def read(args):
            self.calls.append(args)
            if fail and args[0] == fail:
                raise RuntimeError('unavailable')
            if args[0] == 'list-panes':
                return rows
            if args[0] == 'capture-pane':
                return 'old completion\nnew task running'
            if args[-1] == '#{pane_pid}':
                return pid
            return 'value'
        return read

    def test_new_sessions_are_discovered_on_next_snapshot(self):
        first = module.snapshot(self.reader('$1 @1 %1 42'))
        second = module.snapshot(self.reader('$1 @1 %1 42\n$2 @2 %2 42'))
        self.assertEqual(len(first['panes']), 1)
        self.assertEqual(len(second['panes']), 2)
        self.assertEqual(second['coverage'], 'complete')

    def test_linked_pane_is_captured_once_with_all_memberships(self):
        result = module.snapshot(self.reader('$1 @1 %1 42\n$2 @1 %1 42'))
        self.assertEqual(len(result['panes'][0]['memberships']), 2)
        self.assertEqual(sum(c[0] == 'capture-pane' for c in self.calls), 1)
        self.assertTrue(all(c[0] in {'display-message', 'list-panes', 'capture-pane'} for c in self.calls))

    def test_inventory_failure_is_not_empty_success(self):
        result = module.snapshot(self.reader('', fail='list-panes'))
        self.assertEqual(result['coverage'], 'unavailable')

    def test_disappeared_pane_retains_partial_coverage(self):
        result = module.snapshot(self.reader('$1 @1 %1 42', fail='capture-pane'))
        self.assertEqual(result['coverage'], 'partial')
        self.assertIn('error', result['panes'][0])

    def test_restart_during_capture_is_unknown(self):
        result = module.snapshot(self.reader('$1 @1 %1 42', pid='43'))
        self.assertEqual(result['coverage'], 'partial')
        self.assertIn('changed during capture', result['panes'][0]['error'])

    def test_untrusted_inventory_is_never_a_command_target(self):
        result = module.snapshot(self.reader('send-keys -t %1 go on'))
        self.assertEqual(result['coverage'], 'partial')
        self.assertEqual(result['panes'], [])

    def test_snapshot_does_not_classify_old_output_as_completion(self):
        result = module.snapshot(self.reader('$1 @1 %1 42'))
        self.assertNotIn('state', result['panes'][0])


@unittest.skipUnless(shutil.which('tmux'), 'tmux is not installed')
class TmuxIntegrationTests(unittest.TestCase):
    def test_isolated_server_new_session_windows_and_panes(self):
        with tempfile.TemporaryDirectory() as directory:
            socket_path = str(Path(directory) / 'test.sock')
            def read(args):
                result = subprocess.run(['tmux', '-S', socket_path, *args],
                                        capture_output=True, text=True, timeout=10)
                if result.returncode:
                    raise RuntimeError(result.stderr)
                return result.stdout.rstrip('\n')
            try:
                read(['-f', '/dev/null', 'new-session', '-d', '-s', 'initial'])
                first = module.snapshot(read)
                read(['new-session', '-d', '-s', 'new-agent'])
                read(['new-window', '-d', '-t', 'initial'])
                read(['split-window', '-d', '-t', 'initial:0'])
                second = module.snapshot(read)
                self.assertEqual(first['coverage'], 'complete')
                self.assertEqual(len(first['panes']), 1)
                self.assertEqual(second['coverage'], 'complete')
                self.assertEqual(len(second['panes']), 4)
                names = {m['session_name'] for p in second['panes'] for m in p['memberships']}
                self.assertEqual(names, {'initial', 'new-agent'})
            finally:
                # This random test-only socket cannot target the user's server.
                subprocess.run(['tmux', '-S', socket_path, 'kill-server'],
                               capture_output=True, timeout=10)


if __name__ == '__main__':
    unittest.main()
