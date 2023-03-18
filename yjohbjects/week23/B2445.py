# 별 찍기 - 8
# https://www.acmicpc.net/problem/2445

N = int(input())

for i in range(1, N + 1):
    print('*' * i + ' ' * (2* (N - i)) + '*' * i)

for i in range(N - 1, 0, -1):
    print('*' * i + ' ' * (2* (N - i)) + '*' * i)
