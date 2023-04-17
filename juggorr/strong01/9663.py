import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())

# 1차원 배열로 체스판 나타내기
board = [0 for _ in range(N)]

# 퀸을 놓는 위치가 promising한 노드인지 확인하는 함수
def promising(x):
    # 이전에 놓은 체스말들의 위치를 확인하면서
    for i in range(0, x):
        # 1. 같은 row에 있거나 (우에서 훑으면서 내려오기에 같은 col일 수는 없음)
        if (board[i] == board[x] or 
        # 2. 대각선으로 같은 위치에 있다면
        abs(board[i] - board[x]) == abs(i - x)):
            # 프로미싱 하지 않음 출력
            return False
    # 프로미싱함 출력
    return True

# 경우의 수 기록
answer = 0
# col을 타고 내려가면서 퀸을 위치에 놓는 함수
def n_queen(x):
    global answer
    # 종료조건 x가 끝에 다다랏으면 종료
    if x == N:
        answer += 1
        return
    # 세로는 x로 순회하기 때문에 어느 row에 놓을지 정하면 됨
    for row in range(N):
        # 프로미싱한 노드라면
        board[x] = row
        if promising(row):
            # 해당 위치에 퀸 배치
            # 배치된 상태로 다음 col탐색
            n_queen(x + 1)

n_queen(0)
print(answer)