def getzvalues(pattern):
    zvalues = []
    zvalues.append(0)
    r = 0
    l = 0
    for k in range(1, len(pattern[1:])):
        # Case 1: manually compute
        if k > r:
            l, r, zvalue = match_pattern(pattern, 0, k, r, l)
            zvalues.append(zvalue)

        # Case 2
        elif k <= r:
            # kprime usually k - l + 1, but since this is 0-indexed, we are missing one index
            # so it's just k - l
            kprime = k - l
            beta = r - k + 1
            zkprime = zvalues[kprime]

            # Case 2a: if zkprime is less than beta, zk equals zkprime
            if zkprime < beta:
                zvalues.append(zkprime)

            # Case 2b: if zkprime is greater than beta, zk equals beta
            elif zkprime > beta:
                zvalues.append(beta)

            # Case 2c: if zkprime is equal to beta, zkprime equals the length
            # of beta plus the number of matched strings starting
            # at position zkprime + kprime + 1 until a mismatch is reached
            if zkprime == beta:
                pos1 = kprime + beta
                pos2 = k + beta
                l, k, zvalue = match_pattern(pattern, pos1, pos2, r, l)
                zvalues.append(zvalue + beta)
    return zvalues


# pos1 - index on the kprime side
# pos2 - index on the k side
def match_pattern(pattern, pos1, pos2, r, l):
    # print(len(pattern))
    # if pos2 > len(pattern) - 1:
    #     return l, r
    zvalue = 0
    match = False
    for i in pattern[pos2:]:
        # for i in range(pos2, len(pattern[pos2:])):
        # matches
        if i == pattern[pos1]:
            match = True
            zvalue += 1
            pos1 += 1
        # mismatch reached
        else:
            new_r = pos2 + zvalue - 1
            if match and new_r > r:
                r = new_r
                return pos2, r, zvalue
            return l, r, zvalue
    # TODO: flesh out his case when the end of the string
    # is reached with matching characters but there are
    # still suffixes of the string that need zk values
    return l, r, 0


if __name__ == '__main__':
    text = 'abababxysldkjfabababaslkdjfabababa'
    pattern = 'abababa'
    text_pattern = pattern + '$' + text
    print(len(text_pattern))
    zvalues = getzvalues(text_pattern)
    print(zvalues)
