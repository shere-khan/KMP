from knuth_morris_pratt import zalgorithm


class KMP:
    @staticmethod
    def __map_j_to_i(zvalues, spi_primes):
        for j in reversed(range(len(zvalues))):
            i = j + zvalues[j] - 1
            if i > 0:
                spi_primes[i] = zvalues[j]

    @staticmethod
    def __kmp_algorithm(text, pattern, spi_primes):
        occurrences = []
        c = 0
        p = 0
        while c < range(len(text)):
            while pattern[p] is text[c] and p < len(pattern):
                p += 1
                c += 1
            # If position p is equal to the lenght of the pattern, then
            # an occurrence of p was found.
            if p is len(pattern) - 1:
                occurrences.append(c - len(pattern) + 1)
            # Otherwise, if p is 0, then the first character of the pattern
            # was a mismatch with the current position in the text, c. Thus,
            # we increment c by one and continue
            elif p is 0:
                c += 1
            p = KMP.__failure(p, spi_primes)
        return occurrences

    @staticmethod
    def find_pattern(text, pattern):
        # Get Z-values of pattern
        zvalues = []
        zalgorithm.ZAlgorithm.getzvalues(pattern, zvalues)
        print(zvalues)

        # Compute spi prime values of the pattern
        spi_primes = [0] * len(zvalues)
        KMP.__map_j_to_i(zvalues, spi_primes)
        print(spi_primes)

        # find pattern
        return KMP.__kmp_algorithm(text, pattern, spi_primes)

    @staticmethod
    def __failure(i, spi_primes):
        return spi_primes[i - 1] + 1
