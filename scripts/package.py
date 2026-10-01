#!/usr/bin/env python3
"""Build and verify a clean single-directory plugin archive."""
import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path
from validate import ROOT, validate


def build(output):
    manifest = validate()
    output = output.resolve()
    selected = [ROOT / x for x in ('plugin.json', '.codex-plugin/plugin.json', 'README.md', 'CHANGELOG.md')]
    selected += [p for folder in ('skills', 'assets', 'docs') for p in (ROOT / folder).rglob('*') if p.is_file()]
    # docs are linked from README, so ship them as user-facing references too.
    selected = sorted(selected)
    for path in selected:
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError(f'Unsafe package entry: {path}')
        if path.stat().st_size > 5 * 1024 * 1024:
            raise ValueError(f'Unexpected oversized source: {path}')
    if output.is_relative_to(ROOT) and output.parent != ROOT / 'dist':
        raise ValueError('Write archives outside the source tree, or in ignored dist/')
    output.parent.mkdir(parents=True, exist_ok=True)
    prefix = manifest['name'] + '/'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in selected:
            entry = zipfile.ZipInfo(prefix + path.relative_to(ROOT).as_posix(), date_time=(2026, 10, 2, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError('ZIP integrity failure')
        expected = {prefix + p.relative_to(ROOT).as_posix(): p.read_bytes() for p in selected}
        if set(archive.namelist()) != set(expected):
            raise ValueError('Archive inventory mismatch')
        for name, data in expected.items():
            if archive.read(name) != data:
                raise ValueError(f'Archive byte mismatch: {name}')
        with tempfile.TemporaryDirectory() as scratch:
            archive.extractall(scratch)  # only the generated, verified entries above
            validate(Path(scratch) / manifest['name'])
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix + '.sha256').write_text(f'{digest}  {output.name}\n')
    print(json.dumps({'archive': str(output), 'files': len(selected), 'sha256': digest, 'validation': 'passed'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    build(parser.parse_args().output)
