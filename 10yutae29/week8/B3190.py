# B3190_뱀
from collections import deque

N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]

K = int(input())
for _ in range(K):
    i, j = map(int,input().split())
    board[i][j] = 1

L = int(input())

direction = []
for _ in range(L):
    direction.append(input().split())
di_idx = 0


dy = [0, 1, 0, -1] # 우하좌상 (시계방향회전)
dx = [1, 0, -1, 0]
d = 0 # 출발시에는 오른쪽으로 이동함

time = 0 # 이동시간 0으로 초기화


snake = deque([[1, 1]]) # 큐 방식을 사용해서 뱀 움직일거맨

while True:

    y, x = snake[-1][0], snake[-1][1]
    next_y = y + dy[d]
    next_x = x + dx[d]
    time += 1

    # 끝내는 조건
    if (next_y == 0
        or next_y == N+1
        or next_x == 0
        or next_x == N+1
        or [next_y,next_x] in snake):
        break

    # 다음칸으로 이동(길이 늘림)
    snake.append([next_y, next_x])

    # 다음칸에 아무것도 없으면 이동완료(길이 원상회복)
    if board[next_y][next_x] == 0:
        snake.popleft()

    # 다음칸 이동했는데 사과가 있다면
    if board[next_y][next_x] == 1:
        # 사과를 먹음처리/ 몸 길이가 길어졌기 때문에 길이 원상회복 노필요
        board[next_y][next_x] = 0


    # 주어진 시간에 방향을 바꿈
    if time == int(direction[di_idx][0]):
        # D이면 오른쪽으로 회전
        if direction[di_idx][1] == 'D':
            if d == 3:
                d = 0
            else:
                d += 1
        # L이면 왼쪽으로 회전
        else:
            if d == 0:
                d = 3
            else:
                d -= 1

        # 다음 방향전환 정보를 얻기위한 인덱스+1
        if di_idx < len(direction) - 1:
            di_idx += 1

print(time)








