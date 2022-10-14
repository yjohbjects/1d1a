# B6236 용돈관리
# https://www.acmicpc.net/problem/6236

import sys
sys.stdin = open('B6236.txt')

N, M = map(int, input().split())
bankbook = []
for _ in range(N):
    bankbook.append(int(input()))

bankbook = sorted(bankbook)
print(bankbook)

