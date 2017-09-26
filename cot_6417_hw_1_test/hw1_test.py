import unittest
from knuth_morris_pratt import kmp, zalgorithm as z

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

    def test_hw_question_1(self):
        stringa = 'somethingweirder'
        stringb = 'methanedlkfeirder'
        longest_suffix = hw1.Problems.longest_suFfix(stringa, stringb)

        self.assertEqual(longest_suffix, "")

    def test_hw_question_2(self):
        text = 'aabbaxyaba'
        multiset = dict()
        multiset['a'] = 2
        multiset['b'] = 1

        qvalues = list()
        hw1.Problems.find_substrings_of_combos(text, multiset, 3, qvalues)

        self.assertEqual(qvalues, [3, 0, 0, 2, 0, 0, 0, 3, 0, 0])

    def test_hw_question_4a_change_spi_to_spi_prime(self):
        spivalues = [0,0,0,0,0,0,1,2,3,4,0,0,1,2,3,0,1,2,0]
        kmp.KMP.spi_to_spi_prime(spivalues)
        self.assertEqual(spivalues, [0,0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,0,2,0])

    def test_hw_question_4b_change_spi_prime_to_spi(self):
        spiprimevalues = [0,0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,0,2,0]
        kmp.KMP.spiprime_to_spi(spiprimevalues)
        self.assertEqual(spiprimevalues, [0,0,0,0,0,0,1,2,3,4,0,0,1,2,3,0,1,2,0])

    def test_hw_question_3(self):
        text = 'xyaabqcacapmrxyqr'
        pattern = 'aab**aca**rxy'
        zvalues = list()
        z.ZAlgorithm.getzvalues_wildcard(pattern + '$' + text, zvalues)

        answer = [0, 1, 0, 2, 2, 1, 0, 5, 1, 0, 2, 1, 0,
                  0, 0, 0, 13, 1, 0, 2, 2, 1, 0, 5, 1, 0, 2, 1, 0, 0, 0]
        self.assertEqual(zvalues, answer)

if __name__ == '__main__':
    unittest.main()
