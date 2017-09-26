import copy

from knuth_morris_pratt import zalgorithm as z


class Problems:
    @staticmethod
    def __manuallycompare(pattern, i, alphabet_set, qvalues):
        sigma = copy.deepcopy(alphabet_set)
        qvalue = 0
        j = i
        while j < len(pattern) and sigma[pattern[j]] >= 1:
            sigma[pattern[j]] = sigma[pattern[j]] - 1
            j += 1
            qvalue += 1
        qvalues.append(qvalue)
        return j

    @staticmethod
    def multisetsubstrings(text, multiset, sigma_list):
        r = -1
        qvalues = list()
        for k in range(len(text)):
            if k >= r:
                r = Problems.__manuallycompare(text, k, sigma_list[k], qvalues)
            else:
                qvalues.append(0)

        return qvalues

    @staticmethod
    def find_substrings_of_combos(text, multiset, multiset_len, qvalues):
        qval = 0
        # for k, c in enumerate(text):
        k = 0
        while k < (len(text)):
            c = text[k]
            if c in multiset:
                if multiset[c] >= 1:
                    qval += 1
                    multiset[c] -= 1
                else:
                    l = k - qval
                    # l = k + 1 - qval
                    # if text[l] in multiset:
                    multiset[text[l]] = multiset[text[l]] + 1
                    qval -= 1
                    k -= 1
            else:
                for j in range(1, qval + 1):
                    l = k - j
                    multiset[text[l]] = multiset[text[l]] + 1
                qval = 0
            if qval == multiset_len:
                l = k + 1 - qval
                qvalues.append(l)
                multiset[text[l]] = multiset[text[l]] + 1
                qval -= 1
            k += 1

    @staticmethod
    def longest_suffix(stringa, stringb):
        z.ZAlgorithm.getzvalues_longest_suffix()
