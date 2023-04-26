import sys

deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
i = 1

while True:
    N = int(sys.stdin.readline())

    # 종료조건 만족하면 반복문 부수기
    if N == 0:
        break
    
    # 입력받기
    maap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 임의의 무한대 설정
    inf_num = 9 * N * N

    # 우선 다 연결안되어있다고 가정
    visited = [[inf_num] * N for _ in range(N)]
    stack = [(0, 0)]


    # 시작지점 기록
    visited[0][0] = maap[0][0]

    # 우, 하로 이동하면서
    # 해당 좌표의 visited relaxation
    # visited[N - 1][N - 1] 프린트하기
    while stack:
        i, j = stack.pop()

        for delta in deltas:
            ni, nj = i + delta[0], j + delta[1]

            # 그래프 안쪽에 떨어진다면 (재방문해야야하고
            # 방향성 존재해서 맴돌수 X)
            if (0 <= ni < N and 0 <= nj < N):

                if visited[ni][nj] > visited[i][j] + maap[ni][nj]:
                    visited[ni][nj] = visited[i][j] + maap[ni][nj]
                    stack.append((ni, nj))

            # 좌위로도 움직여야대는디..? 맴도는거 어케해결....ㅜ

    # pprint.pprint(visited)
    print(f'Problem {i // 2}:', visited[N - 1][N - 1])
    i += 1

    # 힙큐안써서 개같이 멸망함