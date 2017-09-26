import unittest
from knuth_morris_pratt import kmp, zalgorithm as z

from cot_6417_hw_1 import hw1


class TestProblem2(unittest.TestCase):
    def setUp(self):
        pass

    def test_hw_question_2(self):
        text = 'aabbaxyaba'
        multiset = dict()
        multiset['a'] = 2
        multiset['b'] = 1

        qvalues = list()
        hw1.Problems.find_substrings_of_combos(text, multiset, 3, qvalues)

        self.assertEqual(qvalues, [0,7])

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
