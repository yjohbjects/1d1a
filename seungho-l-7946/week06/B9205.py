# BAEKJOON 9205 - 맥주 마시면서 걸어가기 (S1)

'''
문제
1) 락 페스티벌에 맥주를 마시면서 걸어감. 50미터에 한 병씩 마심
2) 맥주 한 박스를 들고 출발한다. 맥주 한 박스에는 맥주가 20개 들어있음
3) 맥주를 더 구매해야 할 수도 있다. 편의점에 들려, 새 맥주 병을 살 수 있음
4) 박스에 들어있는 맥주는 20병을 넘을 수 없음
5) 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성

풀이
1)

입력
1) 첫째 줄에 테스트 케이스의 개수 t
2) 각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n
3) 다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 두 정수 x와 y로 주어짐
4) 송도는 직사각형 모양으로 생긴 도시임. 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이

출력
1) 각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy"
2) 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력
'''
from pprint import pprint
from collections import deque
import sys

sys.stdin = open('B9205.txt')

# delta
dx = [1, 0]
dy = [0, 1]

def BFS(start, size):
    queue = deque()
    queue.append(start)
    visit[start_x][start_y] = 20

    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= size or ny >= size:
                continue

            if mat[nx][ny] == 3 and visit[nx][ny] == 0:
                return 1

            elif mat[nx][ny] == 2 and visit[nx][ny] == 0:
                visit[nx][ny] = 20
                queue.append((nx, ny))

            elif mat[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] - 1
                if visit[nx][ny] > 0:
                    queue.append((nx, ny))

    return 0

for _ in range(int(input())):

    # input
    N = int(input())
    size = 656
    mat = [[0] * size for _ in range(size)] # 32768 // 50
    visit = [[0] * size for _ in range(size)]

    for i in range(N + 2):
        if i == 0:
            start_x, start_y = map(int, input().split())
            start_x //= 50
            start_y //= 50
            mat[start_x][start_y] = 1
        elif i == (N + 1):
            end_x, end_y = map(int, input().split())
            end_x //= 50
            end_y //= 50
            mat[end_x][end_y] = 3
        else:
            x, y = map(int, input().split())
            x //= 50
            y //= 50
            mat[x][y] = 2

    # output
    result = BFS((start_x, start_y), size)
    if result:
        print('happy')
    else:
        print('sad')