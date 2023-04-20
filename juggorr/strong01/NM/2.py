import sys
import copy 

N, M = map(int, sys.stdin.readline().split())


def NnM2(a1, a2):

    # 꽉찼으면
    if sum(a1) == M:
        if a1 not in a2:
            ac = copy.deepcopy(a1)
            a2.append(ac)

            for i in range(1, N + 1):
                if a1[i]:
                    print(i, end=' ')
            print('')
        return

    for i in range(1, N + 1):
        if not a1[i]:
            a1[i] = 1
            NnM2(a1, a2)
            a1[i] = 0

arr1 = [0] * (N + 1)
arr2 = []

NnM2(arr1, arr2)