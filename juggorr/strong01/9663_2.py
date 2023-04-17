import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())

# 2차원 배열로 체스판 나타내기 (퀸을 위치하는 자리는 1로 표시)
board = [[0] * N for _ in range(N)]

# 대각이동에서 퀸을 발견하기 위한 델타
deltas = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

# promising한 위치인지 확인하는 함수
def promising(col, row):
    #1. 같은 col에 퀸이 있는 경우 => 해당 col의 총합이 0이 아닌 경우
    if sum(board[col]):
        return False
    
    #2. 같은 row에 퀸이 있는 경우
    # => col을 순회하면서
    for i in range(N):
        # 0이 아닌 숫자가 등장하면
        if board[i][row]:
            return False

    #3. 좌우 대각선에 퀸에 있는 경우
    # 해당 좌표에서 4방향 델타이동을하며 퀸을 발견하면 False리턴
    # 한 방향을 정했으면 벗어나거나, 퀸이 등장할 때까지 계속 이동
    for delta in deltas:
        # 벗어나거나, 퀸 등장시 False로 바꾸고 while문 종료
        flag = True
        while flag:
            n_col, n_row = col + delta[0], row + delta[1]
            # 벗어난다면 반복문 종료
            if (n_col < 0 or n_col >= N or n_row < 0 or n_row >= N):
                flag = False
                continue
            # 퀸을 만난다면 False뱉으면서 함수 종료
            if board[n_col][n_row]:
                return False
            
    # 3가지 조건모두 통과시 배치 가능
    return True

# 킹우의 수 세기
answer = 0
# 재귀를 활용해 백트래킹하며 퀸을 놓는 함수
def n_queen(col):
    global answer
    # 칼럼이 N에 달했다면 (N - 1)col에 퀸을 두었다는 뜻 => 킹우의 수에 추가
    if col == N:
        answer += 1
        return
    
    # row를 순회하면서
    for row in range(col, N):
        # 해당 좌표(col, row)가 promising하다면
        if promising(col, row):
            # 해당 좌표에 퀸을 놓고
            board[col][row] = 1
            # 다음 칼럼으로 이동
            n_queen(col + 1)

n_queen(0)
print(answer)