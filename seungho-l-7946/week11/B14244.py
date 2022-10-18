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

from itertools import combinations_with_replacement

# input
N, M = map(int, input().split())
tree = [1] * N

# (N - 2)를 (N - M)개에 나누어서 박기
# (N - 2)까지 수 중에서 (N - M)개 뽑기
numbering = [x for x in range(1, N - 2)]
case_all = list(combinations_with_replacement(numbering, N - M))

# 합이 (N - 2)인 케이스 뽑기
for case in case_all:
    if sum(case) == (N - 2):
        final_case = case
        break

# 케이스에 맞춰서 수 더해주기
for idx in range(len(final_case)):
    tree[idx + 1] += final_case[idx]

# output
for idx in range(len(tree)):
    if tree[idx]:
        for idx2 in range(idx + 1, len(tree)):
            if tree[idx2]:
                print(f'{idx} {idx2}')
                tree[idx] -= 1
                tree[idx2] -= 1
                if not tree[idx]:
                    break