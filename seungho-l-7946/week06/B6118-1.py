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
        v = queue.popleft()
        for w in farm[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1

# input
N, M = map(int, sys.stdin.readline().split())
farm = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    farm[x].append(y)
    farm[y].append(x)

# visited
visited = [0] * (N + 1)

# BFS
BFS(1)

# output
print(visited.index(max(visited)), max(visited) - 1, visited.count(max(visited)))