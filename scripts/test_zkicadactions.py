"""Offline checks for the zkicadactions helpers. Receipts are synthetic; nothing is dispatched or run."""
import copy
import json
import sys
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'skills/zkicadactions'
sys.path.insert(0, str(SKILL / 'scripts'))
import check_receipt  # noqa: E402
import lint_workflow  # noqa: E402

CONFIG = json.loads((SKILL / 'templates/osc-hole-field.config.json').read_text())


def ok(argv, output):
    return {'argv': argv, 'exit_code': 0, 'failure': None, 'output': output}


def smoke_receipt():
    spec = CONFIG['modes']['smoke']
    commands = [ok(c, CONFIG['kicad_version'] + '\n') for c in CONFIG['version_commands']]
    cleanup = [{'status': 'REMOVED_CONFIRMED', 'state_before_cleanup': {'Running': False, 'ExitCode': 0}}
               for _ in range(CONFIG['containers_per_command'] * spec['wrapper_commands'])]
    return {'status': spec['expected_status'], 'source_sha': CONFIG['source_sha'], 'tooling_sha': 'a' * 40,
            'image': CONFIG['image'], 'candidate_ingestion': 'UNIMPLEMENTED', 'commands': commands,
            'before': dict(CONFIG['pins']), 'after': dict(CONFIG['pins']), 'cleanup': cleanup}


TESTS = [ok(['python3'], 'OK'), ok(['python3', '-O'], 'OK')]

WORKFLOW = {
    'on': {'workflow_dispatch': {}}, 'permissions': {'contents': 'read'},
    'concurrency': {'group': 'kicad-' + 'f' * 40, 'cancel-in-progress': False},
    'jobs': {'check': {'runs-on': 'ubuntu-24.04', 'timeout-minutes': 20, 'steps': [
        {'uses': 'actions/checkout@' + 'b' * 40, 'timeout-minutes': 2,
         'with': {'ref': 'f' * 40, 'persist-credentials': False}},
        {'name': 'check', 'timeout-minutes': 9, 'run': 'python3 -B tooling/check.py'},
        {'uses': 'actions/upload-artifact@' + 'c' * 40, 'timeout-minutes': 2,
         'with': {'path': 'upload-safe/receipt.json', 'retention-days': 7, 'if-no-files-found': 'error'}}]}}}


class ReceiptTests(unittest.TestCase):
    def evaluate(self, receipt, status='success', tests=TESTS):
        return check_receipt.evaluate(CONFIG, 'smoke', status, receipt, None, tests)

    def test_good_smoke_passes_only_its_scope(self):
        result = self.evaluate(smoke_receipt())
        self.assertEqual(result['verdict'], 'PASS')
        for dimension in check_receipt.NOT_JUDGED:
            self.assertEqual(result['dimensions'][dimension], 'NOT_EVALUATED')
        self.assertEqual(result['adoption'], 'OWNER_DECISION_REQUIRED')

    def test_version_mismatch_fails(self):
        receipt = smoke_receipt()
        receipt['commands'][0]['output'] = '10.0.5\n'
        self.assertEqual(self.evaluate(receipt)['verdict'], 'FAIL')

    def test_unproven_cleanup_fails(self):
        receipt = smoke_receipt()
        receipt['cleanup'][0] = {'status': 'ABSENT'}
        self.assertEqual(self.evaluate(receipt)['verdict'], 'FAIL')

    def test_unread_artifact_is_unknown(self):
        result = self.evaluate(None, tests=None)
        self.assertEqual(result['verdict'], 'UNKNOWN')
        self.assertIn('do not bypass', result['next_action'])

    def test_candidate_ingestion_claim_fails(self):
        receipt = smoke_receipt()
        receipt['candidate_ingestion'] = 'INGESTED'
        self.assertEqual(self.evaluate(receipt)['verdict'], 'FAIL')

    def test_placeholder_config_is_unknown(self):
        example = json.loads((SKILL / 'templates/project-config.example.json').read_text())
        self.assertEqual(check_receipt.evaluate(example, 'smoke', 'success', smoke_receipt())['verdict'], 'UNKNOWN')


class WorkflowTests(unittest.TestCase):
    def test_contract_workflow_passes(self):
        self.assertEqual(lint_workflow.lint(json.dumps(WORKFLOW), WORKFLOW), [])

    def test_unsafe_workflow_fails(self):
        bad = copy.deepcopy(WORKFLOW)
        bad['permissions'] = {'contents': 'write'}
        bad['jobs']['check']['steps'][0]['with']['persist-credentials'] = True
        bad['jobs']['check']['steps'][1]['run'] = 'git push origin HEAD'
        bad['jobs']['check']['steps'][2]['uses'] = 'actions/upload-artifact@v4'
        findings = lint_workflow.lint(json.dumps(bad), bad)
        for fragment in ('permissions', 'persist-credentials', 'git push', 'pinned'):
            with self.subTest(fragment=fragment):
                self.assertTrue(any(fragment in f for f in findings))


if __name__ == '__main__':
    unittest.main()
