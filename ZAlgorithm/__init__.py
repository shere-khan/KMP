def getzvalues(pattern):
    zvalues = []
    r = 0
    l = 0
    for k in range(1, len(pattern[1:])):
        # Case 1: manually compute
        if k > r:
            match_pattern(pattern, zvalues, 0, k, r, l)

        # Case 2
        elif k <= r:
            zkprime = k - l + 1
            beta = r - k

            # Case 2a: zkprime = zk
            if zkprime < beta:
                pass

            # Case 2b: zkprime = beta
            if zkprime > beta:
                pass

            # Case 2c: zkprime = beta + matched strings starting
            # at position zkprime + kprime + 1
            kprime = "" # TODO ??
            pos1 = kprime + zkprime + -1
            pos2 = k + beta + 1
            if zkprime == beta:
                match_pattern(pattern, zvalues, pos1, pos2, r)


def match_pattern(pattern, zvalues, pos1, pos2, r, l):
    for k in range(pos2, len(pattern[pos2:])):
        for char in range(pos1, len(pattern[pos1:])):
            zvalue = 0
            # matches
            if pattern[k] == char:
                zvalue += 1
                k+=1
            # mismatch reached
            else:
                new_r = k + zvalue - 1
                if new_r > r:
                    r = new_r
                    l = k
                zvalues.append(zvalue)
                break

if __name__ == '__main__':
    for i in range(1, len('justin'[2:])):
        print(i)

    print('hello2')
