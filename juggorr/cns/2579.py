import sys

sys.stdin = open('in.txt')

N = int(sys.stdin.readline())

stairs = [0]
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

print(stairs)

dp = [0 for _ in range(N + 1)]

# for i in range(1, N + 1):
#     dp[i + 1] = 