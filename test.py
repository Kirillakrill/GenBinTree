import unittest
from main import gen_bin_tree


class TestGenTree(unittest.TestCase):
    def test_simple(self):
         self.assertEqual(gen_bin_tree(height=1, root=1), {'1': []})

    def test_level2(self):
         self.assertEqual(gen_bin_tree(height=2, root=1), {'1': [{'2': []}, {'3': []}]})

    def test_level3(self):
        self.assertEqual(gen_bin_tree(height=1, root=5).get('5'), [])


