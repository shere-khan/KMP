def getzvalues(pattern):
    zvalues = []
    zvalues.append(0)
    r = 0
    l = 0
    for k in range(1, len(pattern[1:])):
        # Case 1: manually compute
        if k > r:
            l, r = match_pattern(pattern, zvalues, 0, k, r)

        # Case 2
        elif k <= r:
            # kprime usually k - l + 1, but since this is 0-indexed, we are missing one index
            # so it's just k - l
            kprime = k - l
            beta = r - k
            zkprime = zvalues[kprime]

            # Case 2a: if zkprime is less than beta, zk equals zkprime
            if zkprime < beta:
                zvalues.append(zkprime)

            # Case 2b: if zkprime is greater than beta, zk equals beta
            elif zkprime > beta:
                zk = beta

            # Case 2c: if zkprime is equal to beta, zkprime equals the length
            # of beta plus the number of matched strings starting
            # at position zkprime + kprime + 1 until a mismatch is reached
            pos1 = kprime + beta + 1
            pos2 = k + beta + 1
            if zkprime == beta:
                l, k = match_pattern(pattern, zvalues, pos1, pos2, r)
    return zvalues


# pos1 - index on the kprime side
# pos2 - index on the k side
def match_pattern(pattern, zvalues, pos1, pos2, r):
    zvalue = 0
    for i in pattern[pos2:]:
        # for i in range(pos2, len(pattern[pos2:])):
        # matches
        if i == pattern[pos1]:
            zvalue += 1
            pos1 += 1
        # mismatch reached
        else:
            new_r = pos2 + zvalue - 1
            if new_r > r:
                r = new_r
            zvalues.append(zvalue)
            return pos2, r

if __name__ == '__main__':
    text = 'abababxysldkjfabababaslkdjfabababa'
    pattern = 'abababa'
    text_pattern = pattern + '$' + text
    zvalues = getzvalues(text_pattern)
    print(zvalues)
