import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

# print(numbers)

# checked = [0] * (N + 1)
answer = [0] * (N + 1)

def NnM8(cnt, idx):

    if cnt == M:
        print(*answer[: M])
        return

    for i in range(idx, N):
        answer[cnt] = numbers[i]
        NnM8(cnt + 1, idx)
        answer[cnt] = 0
        idx +=1 

NnM8(0, 0)