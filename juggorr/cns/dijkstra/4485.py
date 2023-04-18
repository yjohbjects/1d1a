import sys
import heapq
sys.stdin = open('in.txt')

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
    visited[0][0] = maap[0][0]
    Q = []
    heapq.heappush(Q, [maap[0][0], (0, 0)])

    while Q:
        val, v = heapq.heappop(Q)

        for delta in deltas:
            ni, nj = v[0] + delta[0], v[1] + delta[1]

            # 맵안에 있다면
            if (0 <= ni < N and 0 <= nj < N):
                
                # relaxation해주면서 힙큐에 넣어주기
                if visited[ni][nj] > visited[v[0]][v[1]] + maap[ni][nj]:
                    visited[ni][nj] = visited[v[0]][v[1]] + maap[ni][nj]
                    heapq.heappush(Q, [maap[ni][nj], (ni, nj)])

    # print(visited)
    print(f'Problem {i}:', visited[N - 1][N - 1])
    i += 1