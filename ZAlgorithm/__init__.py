import ZAlgorithm

if __name__ == '__main__':
    text = 'abababxysldkjfabababaslkdjfabababa'
    pattern = 'abababa'
    text_pattern = pattern + '$' + text
    z = ZAlgorithm.ZAlgorithm()
    print(len(text_pattern))
    zvalues = []
    z.getzvalues(text_pattern, zvalues)
    print(zvalues)
