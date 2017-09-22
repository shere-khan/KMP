import unittest

from knuth_morris_pratt import kmp


class TestKMP(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_pattern_1(self):
        text = 'kwhereisthatwhereisxsdfwhereissdkfwhereisthatwhereisksdl'
        pattern = 'whereisthatwhereisksd'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [34])

    def test_find_pattern_4(self):
        text = 'kwhereisthatwhereisxsdfwhereissdkfwhereisthatwhereisksd'
        pattern = 'whereisthatwhereisksd'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [34])

    def test_find_pattern_9(self):
        text = 'whereisthatwheisxsdfwheresdkfwhereisthatwhereisksd'
        pattern = 'whereisthatwhereisksd'

        # self.assertEqual(kmp.KMP.find_pattern(text, pattern), [33])

    def test_find_pattern_2(self):
        text = 'where'
        pattern = 'where'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [0])

    def test_find_pattern_3(self):
        text = '1where'
        pattern = 'where'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [1])

    def test_find_pattern_6(self):
        text = 'where'
        pattern = 'w'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [0])

    def test_find_pattern_7(self):
        text = 'w'
        pattern = 'w'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [0])

    def test_find_pattern_8(self):
        text = 'w'
        pattern = 'where'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [])

    def test_find_pattern_8(self):
        text = 'w'
        pattern = 'where'

        self.assertEqual(kmp.KMP.find_pattern(text, pattern), [])


if __name__ == '__main__':
    unittest.main()
