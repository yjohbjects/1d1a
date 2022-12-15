# BAEKJOON 2228 - 구간 나누기 1 (G4)

'''
문제
1) N개의 수로 이루어진 1차원 배열에서 M개의 구간을 선택해서, 구간에 속한 수들의 총 합이 최대
2) 각 구간은 한 개 이상의 연속된 수, 서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안 됨, 정확히 M개의 구간
3) N개의 수들이 주어졌을 때, 답을 구하는 프로그램

풀이
1)

입력
1) 첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 배열을 이루는 수들이 차례로 주어진다.

출력
1) 첫째 줄에 답을 출력
'''

import sys

sys.stdin = open('B2228.txt')

from itertools import combinations

# input
N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

# 섹션을 나눌 리스트
com_num = [x for x in range(1, N)]

# 조합을 활용한 섹션 선택
section_list = list(combinations(com_num, M - 1))
print(section_list)
result = []

# dp 선언 및 누적값
# 섹션별로 dp값 나누기
for section in section_list:
    dp = [0] * N
    section = list(section)
    max_value = 0
    for idx in range(len(dp)):
        if idx == 0:
            dp[idx] = numbers[idx]
        else:
            for s in section:
                if idx == s:
                    if dp[idx - 1] > max_value:
                        max_value = dp[idx - 1]
                    dp[idx] = numbers[idx]
                else:
                    dp[idx] = dp[idx - 1] + numbers[idx]
    result.append(max_value)

# output
print(max(result))