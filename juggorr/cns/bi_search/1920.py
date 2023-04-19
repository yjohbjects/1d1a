import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
ns = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().split()))

ns_sort = sorted(ns)
flag = True

for m in ms:

    l, r = 0, N - 1

    while l <= r:
        c = (l + r) // 2

        if ns_sort[c] > m:
            r = c - 1

        elif ns_sort[c] < m:
            l = c + 1

        elif ns_sort[c] == m:
            print(1)
            flag = False
            break

    if flag:
        print(0)
    
    flag = True