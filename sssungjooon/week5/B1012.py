import sys
sys.setrecursionlimit(1000000)

# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
# 농약을 쓰지 않고 배추 재배를 위해 해충 방지에 효과적인 배추흰지렁이 구입
# 지렁이 한마리는 인접한 배추들까지 해충에서 보호한다.
# 0은 배추가 심어져 있지 않은 땅
# 1은 배추가 심어져 있는 땅

# 테스트 케이스를 시행하기 전에 방향과 함수 지정
# 방향부터 설정 (상하좌우)
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

# 전체에서 연결된 배추가 몇 개인지가 아닌, 
# 함수 1회 시행시 연결된 배추 한 세트를 찾는 식으로 진행 
def earthworm(cabbage, r, c) :
    for i in range(4):
        cur_r = r + dr[i]
        cur_c = c + dc[i]

        # 이것이 범위 내라면 계속 탐색
        if cur_c < 0 or cur_c >= M or cur_r < 0 or cur_r >= N :
            continue
        else : 
            # 배추가 있다면 배추 확인하고 0으로 만들고 계속 탐색
            if cabbage[cur_r][cur_c] == 1 :
                cabbage[cur_r][cur_c] = 0
                earthworm(cabbage, cur_r, cur_c)
    return cabbage

# 첫 줄에는 테스트 케이스 개수 T
T = int(input())

# 각 테스트 케이스별 배추밭 가로 길이 M, 세로길이 N, 그리고 배추 개수 K
for test_count in range(T) :
    M, N, K = map(int,input().split())

    # 그 다음에 배추가 심어져 있는 위치가 주어지는데,
    # 우선 배추밭을 만들어준다.
    cabbage = [[0]*M for _ in range(N)]

    # 그리고 지렁이 카운트 변수
    worm = 0

    # 배추 개수 K만큼 반복문을 돌려
    # 배추가 심어져 있는 곳은 1로 만들어준다.
    for _ in range(K):
        x, y = map(int,input().split())
        cabbage[y][x] = 1

    # 전체에서 배추가 있는 곳을 탐색해서 연결된 배추 한 세트씩 없애자
    for c in range(M):
        for r in range(N):
            if cabbage[r][c] == 1 :
                # 각 세트별 시작하는 배추는 0으로 만들고 시작
                cabbage[r][c] = 0
                earthworm(cabbage, r, c)
                worm += 1
    
    print(worm)
    
     