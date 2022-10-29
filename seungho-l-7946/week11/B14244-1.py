# BAEKJOON 14244 - 트리 만들기 (S4)

'''
문제
1) n과 m이 주어졌을 때, n개의 노드로 이루어져 있고, m개의 리프로 이루어져 있는 트리를 만드는 프로그램을 작성
2) 트리는 사이클이 없는 연결 그래프이고, 리프는 차수가 1인 노드를 의미

풀이
1)

입력
1) 첫째 줄에 n과 m

출력
1) 첫째 줄부터 n-1개의 줄에 트리의 간선 정보를 출력한다. 트리의 정점은 0번부터 n-1번까지 이다.
'''

import sys

sys.stdin = open('B14244.txt')

# input
N, M = map(int, input().split())

# [1] - 1 - ... - 1 - 1 - [1,1,...,1](m-1개)

# output
for i in range(N - 1):
    if i <= (N - M):
        print(i, i + 1)
    else:
        print(N - M, i + 1)