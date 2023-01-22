# BAEKJOON 1520 - 내리막 길 (G3)

'''
문제
1) 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능
2) 현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다.
3) 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다.
4) 지도가 주어질 때 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성

풀이
1)

입력
1) 첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어짐
2) M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어짐
3) M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수

출력
1) 첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수
'''

import sys

sys.stdin = open('B1520.txt')

# input
N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * M for _ in range(N)]

stack = [(0, 0)]
visited[0][0] = 1

while stack:
    x, y = stack.pop()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        elif mat[nx][ny] < mat[x][y] and not visited[nx][ny]:
            if nx == (N - 1) and ny == (M - 1):
                visited[nx][ny] = visited[x][y] + 1
                result += 1

            visited[nx][ny] = visited[x][y] + 1
            stack.append((nx, ny))

# num_list = sum(visited, [])
# dp = [0] * (len(num_list) + 1)
# for num in num_list:
#     if num:
#         dp[num] += 1
# print(visited)
# output
print(result)
# if result:
#     print(max(dp))
# else:
#     print(0)