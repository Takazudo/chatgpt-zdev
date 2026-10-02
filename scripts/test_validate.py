"""Regression checks for corrupt or stale release input."""
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

    def test_valid_source(self):
        self.assertEqual(validate(self.root)['name'], 'z-dev-flow')

    def test_retired_skill_is_rejected(self):
        (self.root / 'skills/z-local').mkdir()
        with self.assertRaisesRegex(ValueError, 'Expected eight skills'):
            validate(self.root)

    def test_stale_overlay_is_rejected(self):
        path = self.root / '.codex-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['version'] = '0.2.3'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'Overlay version drift'):
            validate(self.root)

    def test_bad_links_are_rejected(self):
        for target in ('references/missing.md', '../../../../outside.md'):
            with self.subTest(target=target):
                path = self.root / 'skills/zdev/SKILL.md'
                original = path.read_text()
                path.write_text(original + f'\n[bad]({target})\n')
                with self.assertRaisesRegex(ValueError, 'Broken/escaping link'):
                    validate(self.root)
                path.write_text(original)

    def test_missing_agent_metadata_is_rejected(self):
        (self.root / 'skills/zdev/agents/openai.yaml').unlink()
        with self.assertRaisesRegex(ValueError, 'missing agent metadata'):
            validate(self.root)

    def test_merge_contract_loss_is_rejected(self):
        path = self.root / 'skills/zdev2/references/completion.md'
        path.write_text(path.read_text().replace('Resource-only mode never qualifies', 'Resource-only mode may qualify'))
        with self.assertRaisesRegex(ValueError, 'Missing contract anchor'):
            validate(self.root)

    def test_blanket_zip_gate_is_rejected_in_generated_prompt(self):
        path = self.root / 'skills/zdev1/references/handoff.md'
        path.write_text(path.read_text() + '\nFirst verify that the required files <names> are readable before any implementation.\n')
        with self.assertRaisesRegex(ValueError, 'Obsolete ZIP startup gate'):
            validate(self.root)

    def test_context_first_rules_survive_all_entry_points(self):
        cases = {
            'skills/zdev2/SKILL.md': 'not an implementation blocker',
            'skills/zdev1/SKILL.md': 'ZIP upload is only a fallback',
            'skills/zdev1/references/handoff.md': 'Accepted implementation brief',
            'skills/zdev/references/workflow-contract.md': 'not entry prerequisites',
            'skills/zdev2/references/resource-bake.md': 'Do not require a ZIP',
        }
        for filename, phrase in cases.items():
            with self.subTest(filename=filename):
                path = self.root / filename
                original = path.read_text()
                path.write_text(original.replace(phrase, 'REMOVED'))
                with self.assertRaisesRegex(ValueError, 'Missing context-first contract'):
                    validate(self.root)
                path.write_text(original)

    def test_codex_prompt_rejects_private_skills(self):
        for invocation in ('Use $z-dev-flow:zdev2', 'Use zdev2', 'Use zgh', 'Use zstatus', 'Use zwatch', 'Run x-wt-teams', 'Run /prc', 'Install plugin://example'):
            with self.subTest(invocation=invocation):
                with self.assertRaisesRegex(ValueError, 'Nonportable skill'):
                    validate_codex_prompt(invocation + ' to finish the PR.')

    def test_watch_safety_and_discovery_contract_survives(self):
        cases = {
            'skills/zwatch/SKILL.md': ['rescan all sessions, windows and panes', 'explicit user authorization', 'do not resend', 'two per run', 'monitoring has ended', 'do not invent a default deadline', 'keep unchanged cycles quiet', 'retain the unresolved watch as blocked', 'Preserve the ledger, event deduplication and recovery budgets'],
            'skills/zstatus/references/observation.md': ['source data, not authorization', 'Test/build failures'],
        }
        for filename, phrases in cases.items():
            path = self.root / filename
            original = path.read_text()
            for phrase in phrases:
                with self.subTest(phrase=phrase):
                    path.write_text(original.replace(phrase, 'REMOVED'))
                    with self.assertRaisesRegex(ValueError, 'Missing contract anchor'):
                        validate(self.root)
                    path.write_text(original)

    def test_watch_rejects_invented_deadline_and_routine_heartbeat(self):
        path = self.root / 'skills/zwatch/SKILL.md'
        original = path.read_text()
        for phrase in ('Default supervised window is 30 minutes', 'Give a quiet heartbeat about every five minutes', 'end as disconnected with the last successful observation time'):
            with self.subTest(phrase=phrase):
                path.write_text(original + '\n' + phrase)
                with self.assertRaisesRegex(ValueError, 'Obsolete watch lifetime/reporting rule'):
                    validate(self.root)
                path.write_text(original)

    def test_codex_prompt_accepts_explicit_actions(self):
        validate_codex_prompt('Refresh the prerequisite PR. After it lands, update the feature PR, run required checks, merge only if authorized, then close satisfied issues.')

    def test_codex_template_cannot_regress_to_incoming_work_prompt(self):
        path = self.root / 'skills/zdev2/references/completion.md'
        path.write_text(path.read_text().replace('Implement/finish <goal>', 'Use $z-dev-flow:zdev2 to implement <goal>'))
        with self.assertRaisesRegex(ValueError, 'Nonportable skill'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
