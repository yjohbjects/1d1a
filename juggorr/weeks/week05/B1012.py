# 1을 만나면 그 순간부터 주변으로 퍼지는 BFS함수 제작
def BFS(r, c):
    queue = []
    queue.append((r, c))
    # 배추가 있는 곳이고 / 배추벌레를 심지 않은 곳이라면
    if maat[r][c] == 1 and maap[r][c] == 0:
        maap[r][c] = 1

        while queue:
            r, c = queue.pop(0)
            # 배추흰지렁이 델타이동 시키기
            for i in range(4):
                nc, nr = c + dx[i], r + dy[i]
                # 배추흰지렁이가 이동한 곳이 배추밭 안이고 / 배추가 있고 / 방문한 적이 없다면
                if (
                    0 <= nr < N
                    and 0 <= nc < M
                    and maat[nr][nc] == 1
                    and maap[nr][nc] == 0
                ):
                    queue.append((nr, nc))
                    # 방문한 곳의 지도엔 이전 값에 1을 더한값 넣기
                    maap[nr][nc] = maap[r][c] + 1         

T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split())
    # MXN 비어있는 매트릭스 만들기
    maat = [[0] * M for _ in range(N)]
    # 방문기록 표시할 매트릭스 만들기
    maap = [[0] * M for _ in range(N)]
    # 배추흰지렁이 움직이기 / 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    # 그림처럼 채우기
    for _ in range(K):
        c, r = map(int, input().split())
        maat[r][c] = 1
    
    # 모든 원소에 대해 배추흰지렁이 심어보기
    for r in range(N):
        for c in range(M):
            BFS(r, c)
    
    # maap에서 1의 갯수 세기
    count = 0
    for r in range(N):
        for c in range(M):
            if maap[r][c] == 1:
                count += 1

    print(count)