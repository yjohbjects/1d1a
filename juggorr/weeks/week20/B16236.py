from collections import deque
import sys

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def BFS(i, j):
    Q = deque([(i, j)])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while Q:
        v = Q.popleft()

        for di, dj in deltas:
            ni, nj = v[0] + di, v[1] + dj
            
            # 빈칸
            if (0 <= ni < N and 0 <= nj < N
                and visited[ni][nj] == 0
                and bowl[ni][nj] == 0):
                # 이동하자
                Q.append((ni, nj))
                visited[ni][nj] = visited[v[0]][v[1]] + 1
            
            # 대등한칸
            if (0 <= ni < N and 0 <= nj < N
                and visited[ni][nj] == 0
                and bowl[ni][nj] == baby_shark):
                # 이동하자
                Q.append((ni, nj))
                visited[ni][nj] = visited[v[0]][v[1]] + 1

            # 작은칸
            if (0 <= ni < N and 0 <= nj < N
                and visited[ni][nj] == 0
                and bowl[ni][nj] < baby_shark):
                # 이동 멈추고 장바구니
                fishes.append([visited[v[0]][v[1]], ni, nj])
    return

sys.stdin = open('in.txt')
N = int(sys.stdin.readline())
bowl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

baby_shark = 2
timer = 0
eaton = 0

# 아가 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if bowl[i][j] == 9:
            si, sj = i, j

while True:
    # 먹을 수 있는 생선들 넣어줄 리스트
    fishes = []

    # 먹을 수 있는 생선 담기
    BFS(si, sj)

    # 먹을 수 있는 생선 없으면 그 순간이 시합종료
    if not fishes:
        break

    # -(가까운 순, 높이 잇는 순, 왼쪽에 있는 순)으로 정렬 박기
    fishes.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    # 최우선 생선 섭취
    t, fi, fj = fishes.pop()
    # 어항 상태 업데이트
    bowl[si][sj], bowl[fi][fj] = 0, 9
    # 걸린 시간
    timer += t
    # 새 시작 위치
    si, sj = fi, fj
    # 냠냠
    eaton += 1

    # 크기 만큼 먹으면 
    # 하나 커지고 / 다시 크기만큼 먹어야 함
    if eaton == baby_shark:
        baby_shark += 1
        eaton = 0

print(timer)