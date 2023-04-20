import sys

N, M = map(int, sys.stdin.readline().split())

chosen = [0 for _ in range(10)]
is_in = [0 for _ in range(10)]

# print(chosen)
# print(is_in)

def NnM1(arr):

    # 꽉찼으면
    if len(arr) == M:
        for num in arr:
            print(num, end=' ')
        print('')
        return

    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            NnM1(arr)
            arr.pop()

# NnM1([])