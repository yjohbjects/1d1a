# BAEKJOON 1058 - 친구 (S2)

'''
문제
1) 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구함
2) 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재
3) 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람
4) 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램

풀이
1) 각 열별로 DFS를 활용
2) 해당 인원의 2다리 친구까지 탐색하여 해당 수를 카운트함

입력
1) 첫째 줄에 사람의 수 N
2) 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N

출력
1) 첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력
'''

import sys

sys.stdin = open('B1058.txt')

# DFS
def DFS(i):

    # visited
    friend = [0] * N

    # stack
    stack = [i]
    while stack:
        v = stack.pop()

        # 2다리 이상이면 제껴버림
        if friend[v] == 2:
            continue

        # 순회
        for idx in range(len(friends_mat[v])):
            # 친구이며, 자기 자신 외, 아직 관계(visited)아닌 사람
            if friends_mat[v][idx] == 'Y' and idx != i and friend[idx] == 0:
                # 다음 사람
                stack.append(idx)
                # 몇 다리 인가
                friend[idx] = friend[v] + 1

    # 2다리 이내인 사람 count
    cnt = 0
    for f in friend:
        if f:
            cnt += 1

    # 반환
    return cnt

# input
N = int(input())
friends_mat = [list(input()) for _ in range(N)]

# output
result = []
for i in range(N):
    result.append(DFS(i))

# 2다리 내 친구 제일 많은 사람
print(max(result))