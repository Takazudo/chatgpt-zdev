#!/usr/bin/env python3
"""Fail if staged or tracked Git paths include likely private local files.

This complements Gitleaks: it checks filenames, never prints file contents,
and deliberately does not treat .gitignore as a security boundary.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import PurePosixPath

PRIVATE_DIRECTORIES = {".aws", ".gnupg", ".ssh"}
PRIVATE_FILENAMES = {
    ".envrc",
    ".netrc",
    ".npmrc",
    ".pypirc",
    "credentials",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "id_rsa",
    "service-account.json",
    "service_account.json",
}
PRIVATE_SUFFIXES = (".key", ".p12", ".pem", ".pfx", ".tfvars", ".tfvars.json")
SAFE_ENV_EXAMPLE_SUFFIXES = (".example", ".sample", ".template")


def is_sensitive_path(path: str) -> bool:
    parts = [part.lower() for part in PurePosixPath(path).parts]
    if not parts:
        return False

    if any(part in PRIVATE_DIRECTORIES for part in parts[:-1]):
        return True

    name = parts[-1]
    if name in PRIVATE_FILENAMES:
        return True
    if name == ".env" or name.endswith(".env"):
        return True
    if name.startswith(".env.") and not name.endswith(SAFE_ENV_EXAMPLE_SUFFIXES):
        return True
    if name.endswith(PRIVATE_SUFFIXES):
        return True
    return False


def git_paths(mode: str) -> list[str]:
    if mode == "staged":
        command = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"]
    else:
        command = ["git", "ls-files", "--cached", "-z"]

    result = subprocess.run(command, check=True, stdout=subprocess.PIPE)
    return [
        path.decode("utf-8", errors="surrogateescape")
        for path in result.stdout.split(b"\0")
        if path
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="Check the Git index before a commit")
    mode.add_argument("--tracked", action="store_true", help="Check all tracked paths in CI")
    args = parser.parse_args()

    try:
        paths = git_paths("staged" if args.staged else "tracked")
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"Unable to inspect Git paths: {exc}", file=sys.stderr)
        return 2

    blocked = sorted({path for path in paths if is_sensitive_path(path)})
    if blocked:
        print("Blocked: likely sensitive files must not be committed:", file=sys.stderr)
        for path in blocked:
            print(f"  {path}", file=sys.stderr)
        print(
            "Unstage the files, or move non-secret examples to .env.example / .env.sample.",
            file=sys.stderr,
        )
        return 1

    print(f"Sensitive-path check passed ({len(paths)} paths).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
