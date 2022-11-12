# BAEKJOON 11399 - ATM (S4)

'''
문제
1) ATM앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
2) 사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다.
3) 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

풀이
1) sort후, DP를 사용한 합값 구하기

입력
1) 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
2) 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

출력
1) 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
'''

import sys

sys.stdin = open('B11399.txt')

# input
N = int(input())
people_line = list(map(int, input().split()))
people_line.sort()

for idx in range(1, N):
    people_line[idx] += people_line[idx - 1]

result = sum(people_line)

# output
print(result)