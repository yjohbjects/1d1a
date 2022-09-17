# B1012_유기농 배추

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    batchus = []
    for k in range(K):
        i_x, i_y = map(int, input().split())
        batchus.append([i_y, i_x])
    visited = [[0]*M for _ in range(N)]
    dy = [-1, 1, 0, 0]  # 상 하 좌 우
    dx = [0, 0, -1, 1]


    jireong_count = 0       # 필요한 지렁이 수
    stack = []              # 스택 초기화
    stop_count = 0          # 배추를 발견할때마다 배추수를 계산할 변수
    while True:
        for b_y, b_x in batchus:    # dfs의 시작점을 찾아야함
            if visited[b_y][b_x] == 0:  # 만약 조사를 안한 배추라면
                y = b_y                 # y x 에 입력(배추 탐색)
                x = b_x
                visited[y][x] = 1       # 배추 탐색 표시
                stack.append([y, x])    # 스택에 푸쉬 해주기
                stop_count += 1         # 배추 수 + 1
                break

        while stack:                    # 스택에 요소가 있을때
            for w in range(4):          # 위에서 받은 y, x와 인접한 배추를 찾아서~~
                ay = y + dy[w]
                ax = x + dx[w]
                if [ay, ax] in batchus and visited[ay][ax] == 0:    # 주변에 배추가 있고, 확인하지 않은 배추라면
                    y = ay      # 그 배추의 y, x값 받음 즉 그 배추 확인
                    x = ax
                    stack.append([y, x])    # 스택에 푸쉬 해주기
                    visited[y][x] = 1       # 배추 탐색 표시
                    stop_count += 1         # 배추 수 + 1
                    break
            else:                           # 만약 주변에 탐색하지 않은 배추가 없다면
                stack.pop()                 # 스택의 탑을 제거
                if len(stack) != 0:         # 스택이 남았다면
                    y, x = stack[-1]        # y ,x에 스택의 top 값을 넣고 다시 조사

        jireong_count += 1      # 한 구역에 대한 배추를 전부탐색했으면 지렁이 수 + 1

        if stop_count == K:     # 만약 모든 배추를 다 조사했으면
            break               # 반복문 종료

    print(jireong_count)        # 필요한 지렁이 수
