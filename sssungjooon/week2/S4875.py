import sys
sys.stdin = open("4875.txt")

# NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
# 도착할 수 있으면 1, 아니면 0을 출력한다.
# 주어진 미로 밖으로는 나갈 수 없다.
# 마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

# 1은 벽, 0은 통로, 방문했던 곳은 방문하지 않도록 설정

# 방향키 설정 (상하좌우) (로우와 칼럼 각각)
dir_r = [-1, 1, 0, 0]
dir_c = [0 ,0, -1, 1]

# 상하좌우를 순서대로 탐색하는 함수를 만들자
def find_route(maze, cur_r, cur_c) :
    # 상하좌우를 순서대로 탐색
    # cur_r, cur_c는 로우와 컬럼의 현재 위치
    for i in range(4) :
        cur_r += dir_r[i]
        cur_c += dir_c[i]

        # 탐색이 되는 위치라면 (NxN의 범위 안에 있다면)
        if 0 <= cur_r < N and 0 <= cur_c < N :
            # 도착점 3을 찾으면 1을 리턴
            if maze[cur_r][cur_c] == 3 :
                return 1
            # 현재 위치가 통로(0)이고 아직 와본 적 없는 곳이라면 왔다는 표시를 한다.
            elif maze[cur_r][cur_c] == 0 and check[cur_r][cur_c] == 0 :
                check[cur_r][cur_c] = 1
                # 그리고 다시 똑같이 탐색 반복
                if find_route(maze, cur_r, cur_c) :
                    return 1
        # 탐색 종료 후 기존 위치 복귀
        cur_r -= dir_r[i]
        cur_c -= dir_c[i]
    # 탐색이 끝났는데도 도착점을 못찾으면 0을 리턴한다.
    return 0

T = int(input())

# 각 테스트별 판 크기(N)를 입력 후 maze 생성한다.
# 미로 인풋값이 붙어있으므로 split 안하도록 주의
for test_count in range(1, T+1) :
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 해당 좌표 방문기록을 체크할 판(NxN 크기)을 만들자 (각 test_count별 리셋해야 하므로 for문 안으로)
    check = [0 * N for _ in range(N)]

    # 출발지점 2를 찾고 시작 위치 만들기
    for row in range(N) :
        for col in range(N) :
            if maze[row][col] == 2 :
                cur_r = row
                cur_c = col

    # 앞에서 만든 함수에 대해 해당 미로의 결과값 출력
    result = find_route(maze, cur_r, cur_c)
    print(f'#{test_count} {result}')