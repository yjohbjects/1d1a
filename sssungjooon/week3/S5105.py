import sys
sys.stdin = open("5105.txt")

# NxN 크기의 미로에서 출발지 목적지가 주어진다.
# 이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
# 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를,
# 경로가 없는 경우 0을 출력한다.
# 다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
# 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

# 우선적으로 이동 좌표를 만들어놓자
# 상하좌우
move = [(0,1),(0,-1),(-1,0),(1,0)]

# 미로를 찾기 위해 BFS 방식을 이용해보자
def BFS(r, c) :
    global queue
    count = 0
    # 큐가 비면 너비탐색을 완료했으므로
    # 큐가 빌 때까지 반복한다.
    # visited가 빈 리스트면 queue도 빈 리스트가 되고 0 리턴
    while queue :
        visited = []
        while queue :
            # 출발지점 행열(r,c)좌표를 꺼내서
            r, c = queue.pop()
            # 상하좌우 이동
            for i, j in move :
                cur_r = r + i
                cur_c = c + j
                # 해당 좌표가 맵 이내의 범위라면
                if 0 <= cur_r < N and 0 <= cur_c < N :
                    # 통로라면 지나왔다고 방문 표시 후 큐에 추가
                    if not maze[cur_r][cur_c] :
                        maze[cur_r][cur_c] = 1
                        # 좌표를 visited에 추가
                        visited.append((cur_r,cur_c))
                    # 도착지에 도착하면 현재 카운트를 리턴
                    if maze[cur_r][cur_c] == 3 :
                        return count
        # 큐가 빌 때까지 반복되었으면 카운트 올려준다.
        count += 1
        queue = visited
    # 여기까지 했다면 통로는 없다
    return 0

T = int(input())

for test_count in range(1, T+1):
    # 미로의 크기 N 값 인풋
    N = int(input())

    # N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다.
    # 미로를 담을 리스트 준비
    maze = []
    for _ in range(N) :
        data = list(map(int,input().split()))
        maze.append(data)

    # queue와 count 준비
    queue = []
    count = 0

    # 시작지점 2 찾기
    for i in range(N) :
        for j in range(N) :
            if maze[i][j] == 2:
                start_r, start_c = r, c

    # 방문을 했는지 확인하는 판 준비
    visited = [[0]*N for _ in range(N)]

    # 다 됐으면 위에서 정의한 함수 실행
    BFS(start_r, start_c)

    print(f'#{test_count} {count}')
