import sys
from collections import deque
sys.stdin = open('in.txt')

N, M, K = map(int, sys.stdin.readline().split())

maap = [[0] * M for _ in range(N)]

# 음식물 쓰레기 좌표 1로 입력하기
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    maap[i - 1][j - 1] = 1

min_size = 1

# BFS 함수 제작
deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def BFS(v):
    global min_size

    # 기본 사이즈 1로 시작
    size = 1
    visited = [[0] * M for _ in range(N)]
    Q = deque([v])
    maap[v[0]][v[1]] = 2

    while Q:
        # 반복문 밖의 v와 같은 이름으로 써도 될까?
        # 문제없네용~
        v = Q.popleft()

        # 델타 이동
        for delta in deltas:
            ni, nj = v[0] + delta[0], v[1] + delta[1]
            
            # 이동할 수 있다면
            # 방문표시 / 음식물쓰레기 확인 표시 2로 / 사이즈 계산
            if (0 <= ni < N and 0 <= nj < M and
                visited[ni][nj] == 0 and maap[ni][nj] == 1):
                visited[ni][nj] = 1
                maap[ni][nj] += 1
                size += 1
                Q.append((ni, nj))

    # BFS종료 후 현재의 최대 사이즈보다 크다면 갱신
    if size >= min_size:
        min_size = size

# 완전탐색하면서 1을 만나면 BFS탐색 시작
for i in range(N):
    for j in range(M):
        if maap[i][j] == 1:
            BFS((i, j))

print(min_size)