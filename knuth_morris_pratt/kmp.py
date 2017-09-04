class KMP:
    @staticmethod
    def map_j_to_i(zvalues, spi_primes):
        for j in reversed(range(len(zvalues))):
            zvalue = zvalues[j]
            i = j + zvalues[j] - 1
            if i > 0:
                spi_primes[i] = zvalues[j]

    @staticmethod
    def kmp_algorithm(text, pattern):
        pass
