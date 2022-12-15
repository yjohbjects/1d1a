# BAEKJOON 6118 - 숨바꼭질 (S1)

'''
문제
1) 농장에는 헛간이 많이 널려있고 재서기는 그 중에 하나에 숨음. 헛간의 개수는 N(2 <= N <= 20,000)개이며, 1 부터 샌다
2) 수혀니가 1번 헛간부터 찾음. 모든 헛간은 M(1<= M <= 50,000)개의 양방향 길로 이어져 있고, 그 양 끝을 A_i 와 B_i로 나타냄
3) 또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능

풀이
1)

입력
1) 첫 번째 줄에는 N과 M
2) 이후 M줄에 걸쳐서 A_i와 B_i

출력
1) 출력은 한줄로 이루어지며, 세 개의 값을 공백으로 구분지어 출력
2) 첫 번째는 숨어야 하는 헛간 번호를(만약 거리가 같은 헛간이 여러개면 가장 작은 헛간 번호를 출력한다),
두 번째는 그 헛간까지의 거리를, 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력
'''

import sys

sys.stdin = open('B6118.txt')

from collections import deque

# define function
# BFS
def BFS(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        x = queue.popleft()
        for idx in range(len(farm[x])):
            if farm[x][idx] and not visited[idx]:
                queue.append(idx)
                visited[idx] = visited[x] + 1

# input
N, M = map(int, input().split())
farm = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    farm[x - 1][y - 1] = 1
    farm[y - 1][x - 1] = 1

# visited
visited = [0] * N

# BFS
BFS(0)

# 결과 도출
result = []
cnt = 0
for v_idx in range(len(visited)):
    if visited[v_idx] == max(visited):
        cnt += 1
        if cnt == 1:
            result.append(v_idx + 1)
            result.append(visited[v_idx] - 1)
result.append(cnt)

# output
print(" ".join(str(r) for r in result))