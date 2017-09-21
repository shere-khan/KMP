import copy


class Problem2:
    @staticmethod
    def __manuallycompare(pattern, i, alphabet_set, qvalues):
        sigma = copy.deepcopy(alphabet_set)
        qvalue = 0
        j = i
        while sigma[pattern[j]] >= 1:
            sigma[pattern[j]] = sigma[pattern[j]] - 1
            j += 1
            qvalue += 1
        qvalues.append(qvalue)

    @staticmethod
    def multisetsubstrings(text, multiset, alphabet_set):
        k = 0
        r = -1
        qvalues = list()
        for i in range(len(text)):
            if k > r:
                Problem2.__manuallycompare(multiset, k, alphabet_set, qvalues)
            if k + 2 < r:
                qvalues.append(len(multiset))
            qvalues.append(0)
