"""Regression checks for the direct planning-to-Codex contract."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from validate import ROOT, validate, validate_codex_prompt


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'plugin'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', 'dist'))

    def test_valid_source_and_inventory(self):
        self.assertEqual(validate(self.root)['version'], '0.5.0')
        self.assertFalse((self.root / 'skills/zdev2').exists())

    def test_retired_skill_is_rejected(self):
        (self.root / 'skills/zdev2').mkdir()
        with self.assertRaisesRegex(ValueError, 'Expected seven skills'):
            validate(self.root)

    def test_stale_overlay_is_rejected(self):
        path = self.root / '.codex-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['version'] = '0.4.1'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'Overlay version drift'):
            validate(self.root)

    def test_bad_links_are_rejected(self):
        path = self.root / 'skills/zdev/SKILL.md'
        path.write_text(path.read_text() + '\n[bad](references/missing.md)\n')
        with self.assertRaisesRegex(ValueError, 'Broken/escaping link'):
            validate(self.root)

    def test_legacy_alias_routes_all_flags(self):
        alias = (self.root / 'skills/zdev1/SKILL.md').read_text()
        facade = (self.root / 'skills/zdev/SKILL.md').read_text()
        self.assertIn('[zdev](../zdev/SKILL.md)', alias)
        self.assertIn('zdev1 -m -is for https://github.com/zudolab/zudo-text', alias)
        for flag in ('-m', '-pr', '-is', '-isask'):
            self.assertIn(flag, facade)
        self.assertIn('retired zdev2', alias)

    def test_flag_combinations_and_issue_lifecycle(self):
        contract = (self.root / 'skills/zdev/references/workflow-contract.md').read_text()
        for phrase in ('`-isask` wins', '`-isask -m -pr`', 'merge or hold decision for each PR', 'Intentionally held and incomplete PRs remain open', 'Task-specific user constraints override generic flag defaults', 'comment on each original in-scope issue', 'keep delivery issues open pending integration', 'never authorizes deployment'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, contract)

    def test_handoff_instructions_cover_both_merge_modes_and_partial_multi_pr(self):
        handoff = (self.root / 'skills/zdev1/references/handoff.md').read_text()
        for phrase in ('PR plan:', 'each actual or planned PR, target, merge/hold decision', 'Without -m:', 'With -m:', 'intentionally held or incomplete PRs open', 'Do not deploy', 'Do not report a check as passed unless observed', 'do not create a duplicate'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, handoff)

    def test_codex_prompt_rejects_private_skills(self):
        for invocation in ('Use zdev2', 'Use zgh', 'Run x-wt-teams', 'Run /prc', 'Install plugin://example'):
            with self.subTest(invocation=invocation):
                with self.assertRaisesRegex(ValueError, 'Nonportable skill'):
                    validate_codex_prompt(invocation + ' to finish the PR.')

    def test_watch_safety_contract_survives(self):
        path = self.root / 'skills/zwatch/SKILL.md'
        path.write_text(path.read_text().replace('rescan all sessions, windows and panes', 'REMOVED'))
        with self.assertRaisesRegex(ValueError, 'Missing contract anchor'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
