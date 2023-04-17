import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())

board = [0] * N

# 특정 좌표가 promising한지 체크하는 함수
def promising(x):
    
    # 보드를 탐색하면서
    for i in range(x):
        if (board[x] == board[i] or abs(board[i] - board[x]) == abs(x - i)):
            return False
    
    return True

result = 0
def place_q(x):
    global result

    if x == N:
        # 마지막줄에 퀸을 놓는다면
        result += 1
        return
    
    else:
        for i in range(N):
            board[x] = i
            if promising(x):
                place_q(x + 1)
    
place_q(0)
print(result)