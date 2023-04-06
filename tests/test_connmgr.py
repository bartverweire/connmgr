from unittest import TestCase
from connmgr.connmgr import add_two

class TestConnMgr(TestCase):
    def test_add_two(self):
        self.assertEqual(3, add_two(1, 2))


