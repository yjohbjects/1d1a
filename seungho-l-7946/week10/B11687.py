# BAEKJOON 11687 -  (S3)

'''
문제
1) 가장 끝의 0의 개수가 M개인 N! 중에서 가장 작은 N을 찾는 프로그램을 작성

풀이
1)

입력
1) 첫째 줄에 M (1 ≤ M ≤ 100,000,000)

출력
1) 가장 끝의 0의 개수가 M개인 N! 중에서 가장 작은 N을 출력
2) 그러한 N이 없는 경우에는 -1을 출력
'''

import sys

sys.stdin = open('B11687.txt')

# input
M = int(input())
cnt = 0
num = 5
while True:
    tmp = num
    while tmp % 5 == 0:
        tmp //= 5
        cnt += 1
    if cnt == M:
        result = num
        break
    elif cnt > M:
        result = -1
        break
    num += 5

# output
print(result)