N = int(input())

# 배열의 idx가 몇번째 row인지 나타내고, 배열의 값이 col을 나타냄 [1, 0] => (0, 1) (1, 0)
# 0부터 걍쓸거기 때문에 -1로 최초값 설정
board = [-1] * N
# 같은 col에 있으면 안되기 때문에 해당 col을 방문할 수 있는지 체크하는 함수
visited = [0] * N

answer = 0

def can_place_queen(row, col):
    
    for i in range(row):
        if abs(row - i) == abs(board[i] - col):
            return False

    return True

# row: 이번에 퀸을 놓을 행
# cnt: 현재놓여진 퀸의 갯수
def nqueen(row, cnt):
    global answer
    
    if row == N:
        answer +=1
        return
    
    for i in range(N):
        # 해당 col에 아무퀸도 없고, 대각선에도 퀸이 없다면
        if not visited[i] and can_place_queen(row, i):
                # 해당 col 방문표시
                visited[i] = 1
                # 해당열에 col값 넣기
                board[row] = i
                # 다음 row 탐색
                nqueen(row + 1, cnt + 1)
                # 방문표시 제거
                visited[i] = 0
                board[row] = -1

nqueen(0, 0)
print(answer)