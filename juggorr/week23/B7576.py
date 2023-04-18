from pprint import pprint
from collections import deque
import sys
sys.stdin = open('in2.txt')

M, N = map(int, sys.stdin.readline().split())

tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

Q = deque([])
# 익은 토마토(1) 발견하면 BFS돌려주기
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            Q.append((i, j))

# 그냥 BFS
def BFS():

    while Q:
        i, j = Q.popleft()

        for delta in deltas:
            ni, nj = i + delta[0], j + delta[1]

            if (0 <= ni < N and 0 <= nj < M and
                tomatoes[ni][nj] == 0):
                Q.append((ni, nj))
                tomatoes[ni][nj] = tomatoes[i][j] + 1

BFS()

pprint(tomatoes)

day_counter = 1

# 완전탐색
# 안익은 토마토(0) 발견하면 -1 출력하고 
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            print(-1)
            # 프로그램 종료
            exit(0)
        # 토마토 익은날짜 큰걸로 바꾸기
        if tomatoes[i][j] > day_counter:
            day_counter = tomatoes[i][j]

print(day_counter - 1)