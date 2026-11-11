#!/usr/bin/env python3
"""Regression tests for sensitive filename checks (including a real Git index)."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from check_sensitive_paths import is_sensitive_path


SCRIPT = Path(__file__).with_name("check_sensitive_paths.py")


class SensitivePathRulesTest(unittest.TestCase):
    def test_rejects_private_file_patterns(self):
        for path in (
            ".env",
            ".env.production",
            "nested/.env.local",
            "prod.env",
            "nested/.envrc",
            ".npmrc",
            "config/.pypirc",
            ".netrc",
            "id_ed25519",
            ".ssh/id_rsa",
            ".aws/credentials",
            "config/token.pem",
            "config/private.key",
            "certs/client.p12",
            "secrets/production.tfvars",
            "secrets/production.tfvars.json",
            "service-account.json",
        ):
            with self.subTest(path=path):
                self.assertTrue(is_sensitive_path(path))

    def test_allows_documented_examples_and_normal_files(self):
        for path in (
            ".env.example",
            ".env.sample",
            ".env.template",
            "nested/.env.production.example",
            "nested/.env.local.sample",
            "config/app.json",
            ".github/workflows/security.yml",
            "docs/credentials-guide.md",
            "scripts/test_sensitive_paths.py",
        ):
            with self.subTest(path=path):
                self.assertFalse(is_sensitive_path(path))


@unittest.skipUnless(shutil.which("git"), "git is required for the integration test")
class SensitivePathGitIndexTest(unittest.TestCase):
    def test_staged_and_tracked_checks_block_forced_secrets(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            (repo / ".gitignore").write_text(".env\n", encoding="utf-8")
            (repo / ".env.example").write_text("API_KEY=placeholder\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", ".gitignore", ".env.example"], check=True)

            def scan(mode):
                return subprocess.run(
                    [sys.executable, str(SCRIPT), mode],
                    cwd=repo,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=False,
                )

            self.assertEqual(scan("--staged").returncode, 0)
            self.assertEqual(scan("--tracked").returncode, 0)

            # .gitignore is not a security boundary: git add -f can override it.
            (repo / ".env").write_text("EXAMPLE_SECRET=not-a-real-secret\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", "-f", ".env"], check=True)
            self.assertEqual(scan("--staged").returncode, 1)
            self.assertEqual(scan("--tracked").returncode, 1)
            self.assertIn(".env", scan("--staged").stderr)


if __name__ == "__main__":
    unittest.main()
