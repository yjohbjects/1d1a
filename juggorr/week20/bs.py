from collections import deque
import sys
sys.stdin = open('in.txt')

# 상 좌 하 우
deltas = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def BFS(r, c):
    global baby_shark
    global timer
    global eaten

    Q = deque([[r, c]])
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1

    while Q:
        v = Q.popleft()
        for delta in deltas:
            nr, nc = v[0] + delta[1], v[1] + delta[0]


            if 0 <= nr < N and 0 <= nc < N:
            # 이동할 수 있다면
                if (visited[nr][nc] == 0
                    and bowl[nr][nc] <= baby_shark):
                    # 빈 칸 이라면
                    if bowl[nr][nc] == 0:
                        Q.append([nr, nc])
                        visited[nr][nc] = visited[v[0]][v[1]] + 1

                    # 같은 크기의 물고기라면
                    elif bowl[nr][nc] == baby_shark:
                        Q.append([nr, nc])
                        visited[nr][nc] = visited[v[0]][v[1]] + 1

                    # 잡아먹는 경우
                    else:
                        timer += visited[v[0]][v[1]]
                        eaten += 1
                        bowl[nr][nc] = 9
                        bowl[sr][sc] = 0

                        if eaten == baby_shark:
                            baby_shark += 1
                            eaten = 0

                        break
    return

N = int(sys.stdin.readline())
bowl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

baby_shark = 2
timer = 0
eaten = 0
edible = True

while edible:
    small_fishes = 0
    sr, sc = 0, 0

    for r in range(N):
        for c in range(N):
            if bowl[r][c] < baby_shark and bowl[r][c] != 0:
                small_fishes += 1
            if bowl[r][c] == 9:
                sr, sc = r, c
    print(sr, sc)

    # 반복문 종료조건
    if not small_fishes:
        edible = False

    else:
        # BFS로 한마리 잡아먹고 eaten 카운트 1 증가
        # visited 초기화 갈기고, bowl 상태 업데이트
        # eaten == baby_shark가 되면 baby_shark += 1해주고 eaten 초기화
        BFS(sr, sc)
        # print(eaten)

# print(timer)