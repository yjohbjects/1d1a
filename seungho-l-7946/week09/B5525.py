# BAEKJOON 5525 - IOIOI (S1)

'''
문제
1) N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN
2) I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램
ex)
P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)

풀이
1)

입력
1) 첫째 줄에 N이 주어진다.
2) 둘째 줄에는 S의 길이 M이 주어지며
3) 셋째 줄에 S

출력
1) S에 PN이 몇 군데 포함되어 있는지 출력
'''

import sys

sys.stdin = open('B5525.txt')

def BruteForce(pattern, text, result):
    n = len(text)
    m = len(pattern)
    i = 0
    j = 0
    while i < n:
        if text[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1

        if j == m:
            result += 1
            i -= (j - 1)
            j = 0
    return result

# input
N = int(input())
M = int(input())
S = input()

# PN IOI
PN = ''
for i in range(2 * N + 1):
    if i % 2 == 0:
        PN += 'I'
    else:
        PN += 'O'

# BruteForce 1 13 OOIOIOIOIIOII
result = 0
result = BruteForce(PN, S, result)

# output
print(result)