import unittest

from knuth_morris_pratt import zalgorithm as z


class TestKMP(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_find_pattern_2(self):
        text = 'abababxysldkjfabababaslkdjfabababa'
        pattern = 'abababa'
        zvalues = list()
        answer = [0, 0, 5, 0, 3, 0, 1, 0, 6, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 7, 0, 5, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 7, 0, 5, 0, 3, 0, 1]
        z.ZAlgorithm.getzvalues(pattern + '$' + text, zvalues)

        self.assertEqual(zvalues, answer)


if __name__ == '__main__':
    unittest.main()
