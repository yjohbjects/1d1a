import sys
sys.stdin = open('in.txt')

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    tree = [0 for _ in range(N + 1)]

    cnt = 0
    while N > 1:
        N = N // 2
        cnt += 1

    tree[2**cnt] = 1

    