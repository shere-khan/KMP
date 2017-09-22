import unittest

from cot_6417_hw_1 import hw1


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.alphabet_dict = dict()
        self.alphabet_dict['a'] = 2
        self.alphabet_dict['b'] = 1
        self.alphabet_dict['c'] = 0
        self.alphabet_dict['d'] = 0
        self.alphabet_dict['e'] = 0
        self.alphabet_dict['f'] = 0
        self.alphabet_dict['g'] = 0
        self.alphabet_dict['h'] = 0
        self.alphabet_dict['i'] = 0
        self.alphabet_dict['j'] = 0
        self.alphabet_dict['k'] = 0
        self.alphabet_dict['l'] = 0
        self.alphabet_dict['m'] = 0
        self.alphabet_dict['n'] = 0
        self.alphabet_dict['o'] = 0
        self.alphabet_dict['p'] = 1
        self.alphabet_dict['q'] = 0
        self.alphabet_dict['r'] = 0
        self.alphabet_dict['s'] = 0
        self.alphabet_dict['t'] = 0
        self.alphabet_dict['u'] = 0
        self.alphabet_dict['v'] = 0
        self.alphabet_dict['w'] = 0
        self.alphabet_dict['x'] = 0
        self.alphabet_dict['y'] = 0
        self.alphabet_dict['z'] = 0

    def test_find_pattern_1(self):
        text = 'aabbaxyaba'
        multiset = 'aab'
        sigma_list = [self.alphabet_dict] * len(text)
        qvalues = hw1.Problem2.multisetsubstrings(text, multiset, sigma_list)

        self.assertEqual(qvalues, [3, 0, 0, 2, 0, 0, 0, 3, 0, 0])


if __name__ == '__main__':
    unittest.main()
