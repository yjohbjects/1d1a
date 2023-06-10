import sys
sys.stdin = open('in.txt')

# 최대크기 100까지의 보드 제작
board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    # 주어진 리스트 순회하면서 숫자4개 구하기
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    # 해당 숫자위치에서 박스가 아닌 점으로 크기 구하기
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

answer = 0
# row순회하면서 값 더해주기
for row in board:
    answer += sum(row)
print(answer)