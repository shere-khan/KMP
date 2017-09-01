def getzvalues(pattern):
    zvalues = []
    r = 0
    l = 0
    for k in range(1, len(pattern[1:])):
        # Case 1: manually compute
        if k > r:
            l, k = match_pattern(pattern, zvalues, 0, k, r, l)

        # Case 2
        elif k <= r:
            kprime = k - l + 1
            beta = r - k
            zkprime = zvalues[kprime]

            # Case 2a: if zkprime is less than beta, zk equals zkprime
            if zkprime < beta:
                zvalues.append(zkprime);

            # Case 2b: if zkprime is greater than beta, zk equals beta
            if zkprime > beta:
                pass

            # Case 2c: if zkprime is equal to beta, zkprime equals the length
            # of beta plus the number of matched strings starting
            # at position zkprime + kprime + 1 until a mismatch is reached
            kprime = k - l + 1;
            pos1 = kprime + zkprime + -1
            pos2 = k + beta + 1
            if zkprime == beta:
                match_pattern(pattern, zvalues, pos1, pos2, r)


def case2a():
    pass

def case2b():
    pass

def case2c():
    pass


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
                    return l, k
                zvalues.append(zvalue)
                break

if __name__ == '__main__':
    for i in range(1, len('justin'[2:])):
        print(i)

    print('hello2')
