import unittest

from knuth_morris_pratt import zalgorithm as z


class TestKMP(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_pattern_1(self):
        text = 'xyaabqcacapmrxyqr'
        pattern = 'aab**aca**rxy'
        zvalues = list()
        z.ZAlgorithm.getzvalues_wildcard(pattern + '$' + text, zvalues)

        self.assertEqual(zvalues, [0])


if __name__ == '__main__':
    unittest.main()
