from knuth_morris_pratt import zalgorithm, keywordtree, kmp

if __name__ == '__main__':
    z = zalgorithm.ZAlgorithm()
    # text = 'abababxysldkjfabababaslkdjfabababa'
    # pattern1 = 'abababa'
    # text_pattern = pattern1 + '$' + text
    # zvalues1 = []
    # z.getzvalues(text_pattern, zvalues)

    text = 'whereilwherkwheredfwhejswdlwhereiskwhere'
    pattern2 = 'whereis'
    occurrences = kmp.KMP.find_pattern(text, pattern2)
    print(occurrences)

    # Construct keyword tree out of patterns in P
    # tree = keywordtree.KeywordTree()
    # P = ['password', 'passive', 'passover', 'heavy']
    # for i, p in enumerate(P):
    #     tree.insert(p, i + 1)

    # tree.dfs(print)


