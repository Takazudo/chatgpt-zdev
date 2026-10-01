"""Regression checks for corrupt or stale release input."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from validate import ROOT, validate


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
        with self.assertRaisesRegex(ValueError, 'Expected six skills'):
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


if __name__ == '__main__':
    unittest.main()
