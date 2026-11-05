"""Offline tests: python3 -m unittest discover -s scripts -p 'test_*.py'."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

import check_updates as checks


class DailyChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name) / 'state.sqlite3'
        self.now = datetime(2026, 11, 5, 23, 59, tzinfo=timezone(timedelta(hours=8)))

    def test_same_day_shared_and_midnight(self):
        calls = []
        def probe():
            calls.append(1)
            return {'version': '1.6.0'}
        self.assertFalse(checks.daily(self.db, 'registry', probe, self.now)[1])
        self.assertTrue(checks.daily(self.db, 'registry', probe, self.now)[1])
        self.assertFalse(checks.daily(self.db, 'registry', probe, self.now + timedelta(minutes=2))[1])
        self.assertEqual(len(calls), 2)

    def test_failure_is_cached(self):
        def fail():
            raise OSError('sensitive diagnostic')
        result, _, _ = checks.daily(self.db, 'a', fail, self.now)
        self.assertEqual(result, {'status': 'unavailable', 'error_type': 'OSError'})
        self.assertTrue(checks.daily(self.db, 'a', lambda: self.fail('network repeated'), self.now)[1])

    def test_channels_independent(self):
        checks.daily(self.db, 'git', lambda: {}, self.now)
        self.assertFalse(checks.daily(self.db, 'registry', lambda: {}, self.now)[1])

    def test_concurrent_reservation(self):
        entered, release = threading.Event(), threading.Event()
        def slow():
            entered.set()
            release.wait(3)
            return {}
        worker = threading.Thread(target=lambda: checks.daily(self.db, 'git', slow, self.now))
        worker.start()
        try:
            self.assertTrue(entered.wait(3))
            result, cached, _ = checks.daily(self.db, 'git', lambda: self.fail('duplicate'), self.now)
            self.assertTrue(cached)
            self.assertEqual(result['status'], 'pending_or_interrupted')
        finally:
            release.set()
            worker.join()

    def test_registry_notification_only_once_and_local_recompare(self):
        root = Path(self.temp.name)
        manifest = root / 'SKILL.md'
        manifest.write_text('---\nversion: 1.5.0\n---\n')
        with patch.object(checks, 'query', return_value={'version': '1.6.0'}) as query:
            self.assertTrue(checks.check(root, self.db)['notify'])
            self.assertFalse(checks.check(root, self.db)['notify'])
            manifest.write_text('---\nversion: 1.6.0\n---\n')
            self.assertEqual(checks.check(root, self.db)['comparison'], 'not_newer')
            query.assert_called_once()

    def test_unknown_origin_not_contacted(self):
        root = Path(self.temp.name)
        (root / '.git').mkdir()
        with patch.object(checks, 'run', return_value='https://untrusted.example/repo.git'):
            with self.assertRaises(ValueError):
                checks.source(root)


if __name__ == '__main__':
    unittest.main()
