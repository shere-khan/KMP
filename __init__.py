from knuth_morris_pratt import keywordtree, kmp

if __name__ == '__main__':
    # text = 'kwhereisthatwhereisxsdfwhereissdkfwhereisthatwhereisksdl'
    # pattern2 = 'whereisthatwhereisksd'
    text = 'w'
    pattern2 = 'where'
    # pattern2 = 'where'
    occurrences = kmp.KMP.find_pattern(text, pattern2)
    print(occurrences)

    # Construct keyword tree out of patterns in P
    # tree = keywordtree.KeywordTree()
    # P = ['password', 'passive', 'passover', 'heavy']
    # for i, p in enumerate(P):
    #     tree.insert(p, i + 1)

    # tree.dfs(print)


