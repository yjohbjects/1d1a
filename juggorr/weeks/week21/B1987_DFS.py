import sys
sys.stdin = open('in.txt')

# 행, 렬, 행렬 입력받기
R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# 최대 칸 수
MAX_cnt = 1

# 델타 / 하 우 상 좌
deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 이동한 알파벳 배열
alphas = set(arr[0][0])

# 재귀 DFS
# 로우, 칼람, 칸 수
def DFS(sr, sc, cnt):
    global MAX_cnt

    # 최대거리 갱신
    if cnt > MAX_cnt:
        MAX_cnt = cnt

    # 이동하자 이동
    for delta in deltas:
        nr, nc = sr + delta[0], sc + delta[1]

        # 범위안에 있고 / 배열에 없다면
        if (0 <= nr < R and 0 <= nc < C and
            arr[nr][nc] not in alphas):
            alphas.add(arr[nr][nc])
            
            # 해당 방향으로 진행
            DFS(nr, nc, cnt + 1)
            
            # 진행멈추면 부모노드로 돌아가기
            alphas.remove(arr[nr][nc])

# 시작점, 시작점 부터 1칸
DFS(0, 0, 1)
print(MAX_cnt)