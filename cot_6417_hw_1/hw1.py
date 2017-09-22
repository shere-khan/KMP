import copy


class Problem2:
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
                r = Problem2.__manuallycompare(text, k, sigma_list[k], qvalues)
            else:
                qvalues.append(0)

        return qvalues

