# BAEKJOON 2583 - 영역 구하기 (S1)

'''
문제
1) 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이
2) 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나뉨
3) M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역
4) 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램

풀이
1) BFS와 count를 함께 진행

입력
1) 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어짐. M, N, K는 모두 100 이하의 자연수
2) 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어짐
3) 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)
4) 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없음

출력
1) 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력
2) 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력
'''

import sys

sys.stdin = open('B2583.txt')

from collections import deque

# input
M, N, K = map(int, input().split())

# 좌표 평면
plane = [[0] * N for _ in range(M)]

# 영역 전개
for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for y in range(sy, ey):
        for x in range(sx, ex):
            plane[y][x] = 1

# delta
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def BFS(start):
    answer = 1

    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if plane[nx][ny] == 0:
                plane[nx][ny] = 1
                queue.append((nx, ny))
                answer += 1

    return answer

# 결과값 변수 선언
result = []
cnt = 0

# 영역 구하기
for i in range(M):
    for j in range(N):
        if plane[i][j] == 0:
            plane[i][j] = 1
            result.append(BFS((i, j)))
            cnt += 1

result.sort()

# output
print(cnt)
print(" ".join(str(r) for r in result))