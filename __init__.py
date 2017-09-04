from knuth_morris_pratt import zalgorithm, keywordtree, kmp

if __name__ == '__main__':
    z = zalgorithm.ZAlgorithm()
    # text = 'abababxysldkjfabababaslkdjfabababa'
    # pattern1 = 'abababa'
    # text_pattern = pattern1 + '$' + text
    # zvalues1 = []
    # z.getzvalues(text_pattern, zvalues)

    pattern2 = 'whereislwherkdfwhejswdlwhkwhereis'
    zvalues2 = []
    z.getzvalues(pattern2, zvalues2)
    print(zvalues2)
    spi_primes = [0] * len(zvalues2)
    kmp.KMP.map_j_to_i(zvalues2, spi_primes)
    print(spi_primes)

    # tree = keywordtree.KeywordTree()
    # P = ['password', 'passive', 'passover', 'heavy']
    # for i, p in enumerate(P):
    #     tree.insert(p, i + 1)

    # tree.dfs(print)
