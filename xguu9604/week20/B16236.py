from collections import deque

'''
상어 쉑 그냥 주는대로 먹지
먹을수 있고 갈 수 있는지 확인하고 거리 최솟값 찾기
'''


# 범위 내에 존재하는 좌표인지 확인
def is_in(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


# BFS를 통해서 먹으러 가기
# x, y: 현재 상어 좌표, to_go: 먹이 위치, size: 상어 크기
def BFS(x, y, N, sea, to_go, size):
    Q = deque()
    Q.append((x, y))
    visited = [[0] * N for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[x][y] = 1
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            now_i = i + dx[k]
            now_j = j + dy[k]
            # 현재 먹으러 간 먹이에 도착했다면 이동 거리 반환
            if now_i == to_go[0] and now_j == to_go[1]:
                return visited[i][j]
            # 바다 안의 좌표이며 아직 방문한적 없고 지나가는 곳이 상어 사이즈 이하면 지나가자!
            elif is_in(now_i, now_j) and not visited[now_i][now_j] and sea[now_i][now_j] <= size:
                Q.append((now_i, now_j))
                visited[now_i][now_j] = visited[i][j] + 1
    # 반복 전부 끝났는데 도착 못하면 False 반환
    return False


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

# 상어 좌표를 받을 변수
shark_x = 0
shark_y = 0
# 아가 상어의 이동거리
answer = 0
# 아가 상어의 크기
shark_size = 2

# 아가 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sea[i][j] = 0
            shark_x = i
            shark_y = j
            break

# 아가 상어의 레벨업까지 먹은 먹이수
eaten = 0
# 반복 탈출을 위한 조건
can_eat = True
while can_eat:
    can_eat = False
    # 먹을 먹이
    preys = []
    # 최소 이동거리
    min_dis = N * N
    for i in range(N):
        for j in range(N):
            # 일단 물고기가 있으면
            if sea[i][j]:
                # 그 물고기가 먹을수 있는 물고기이면
                if sea[i][j] < shark_size:
                    # 일단 먹으러 가보자
                    dis = BFS(shark_x, shark_y, N, sea, [i, j], shark_size)
                    # 갈 수 있으며 현재 제일 가까운 먹이라면
                    # 거리가 같다면 제일 좌 상단으로 가는 조건이므로
                    # 같은 거리라면 이전 먹이보다 오른쪽 혹은 아래 있는 먹이라 세어줄 필요가 없음
                    if dis and dis < min_dis:
                        # 최소 거리 최신화
                        min_dis = dis
                        # 먹으러 갈 먹이로 지정
                        preys = [i, j, dis]
                        can_eat = True

    # 만약 먹을 먹이가 있다면
    if preys:
        # 거리 추가해주고
        answer += preys[2]
        # 먹이는 없애주고
        sea[preys[0]][preys[1]] = 0
        # 경험치 쌓고
        eaten += 1
        # 아가 상어를 그쪽으로 이동
        shark_x = preys[0]
        shark_y = preys[1]

        # 경험치가 아가 상어 크기가 되면
        if eaten == shark_size:
            # 경험치 초기화 하고
            eaten = 0
            # 아가상어 레벨업
            shark_size += 1

print(answer)

