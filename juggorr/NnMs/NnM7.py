import sys

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

# print(numbers)

# checked = [0] * (N + 1)
answer = [0] * (N + 1)

def NnM7(cnt):

    if cnt == M:
        print(*answer[: M])
        return

    for i in range(N):
        answer[cnt] = numbers[i]
        NnM7(cnt + 1)
        answer[cnt] = 0

NnM7(0)