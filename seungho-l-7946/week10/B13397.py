# BAEKJOON 13397 - 구간 나누기 2 (G4)

'''
문제
1) N개의 수로 이루어진 1차원 배열이 있다. 이 배열을 M개 이하의 구간으로 나누어서 구간의 점수의 최댓값을 최소로함
2) 하나의 구간은 하나 이상의 연속된 수, 배열의 각 수는 모두 하나의 구간에 포함
3) 구간의 점수란 구간에 속한 수의 최댓값과 최솟값의 차이
4) 배열과 M이 주어졌을 때, 구간의 점수의 최댓값의 최솟값을 구하는 프로그램을 작성

풀이
1)

입력
1) 첫째 줄에 배열의 크기 N과 M
2) 둘째 줄에 배열에 들어있는 수가 순서대로 주어진다. 배열에 들어있는 수는 1보다 크거나 같고, 10,000보다 작거나 같은 자연수

출력
1) 첫째 줄에 구간의 점수의 최댓값의 최솟값을 출력
'''

import sys

sys.stdin = open('B13397.txt')

from itertools import combinations

def scoring(list_x):
    return max(list_x) - min(list_x)

# input
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

com_num = [x for x in range(1, N)]
section_list = list(combinations(com_num, M - 1))

result = max(numbers)
for section in section_list:
    section = [0] + list(section) + [N]

    max_value = 0
    for idx in range(1, len(section)):
        temp = numbers[section[idx - 1]:section[idx]]
        if scoring(temp) > max_value:
            max_value = scoring(temp)

    if max_value < result:
        result = max_value

# output
print(result)