import unittest
from solution import sortline

class TestSortline(unittest.TestCase):

    def test_single_int(self):
        self.assertEqual(sortline('1'), '1')
        self.assertEqual(sortline('-1'), '-1')

    def test_only_strs(self):
        self.assertEqual(sortline('car truck bus'), 'bus car truck')
        self.assertEqual(sortline('d c b a'), 'a b c d')

    def test_only_ints(self):
        self.assertEqual(sortline('8 4 6 1 -2 9 5'), '-2 1 4 5 6 8 9')

    def test_mixed(self):
        inp = "car truck 8 4 bus 6 1"
        exp = "bus car 1 4 truck 6 8"
        self.assertEqual(sortline(inp), exp)

    def test_weird(self):
        self.assertEqual(sortline("3a -2 sample -3"), "3a -3 sample -2")

if __name__ == '__main__':
    unittest.main()
