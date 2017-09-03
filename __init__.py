# from kmp import zalgorithm
from kmp import tree

if __name__ == '__main__':
    # text = 'abababxysldkjfabababaslkdjfabababa'
    # pattern = 'abababa'
    # text_pattern = pattern + '$' + text
    # z = zalgorithm.ZAlgorithm()
    # print(len(text_pattern))
    # zvalues = []
    # z.getzvalues(text_pattern, zvalues)
    # print(zvalues)

    tree = tree.KeywordTree()
    P = ['password', 'passive', 'passover', 'heavy']
    for i, p in enumerate(P):
        tree.insert(p, i + 1)

    tree.dfs(print)
