# BAEKJOON 10026 - 적록색약 (G5)

'''
문제
1) 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
2) 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
3) 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
4) 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
5) 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

풀이
1) DFS 사용
2) R과 G를 같은 글자로 인식하도록 조건문 추가
'''

from pprint import pprint
import sys

sys.stdin = open('B10026.txt')

# input
N = int(input())
mat = [list(map(str, input())) for _ in range(N)]

# 적록색약이 보는 세상
mat_RG = [[''] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        mat_RG[i][j] = mat[i][j]
        if mat_RG[i][j] == 'R':
            mat_RG[i][j] = 'G'

# delta
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs
def dfs(i, j, N, matrix):

    # 영역 카운트
    cnt = 0

    # 매트릭스 값이 있다면
    if matrix[i][j]:

        # 시작하는 좌표의 값 저장
        tmp = matrix[i][j]

        # 스택 시작
        stack = [(i, j)]
        while stack:

            # 탐색 좌표 뽑기
            x, y = stack.pop()

            # 값 삭제 - visit
            matrix[x][y] = ''

            # delta
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 매트릭스 바깥 제외
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                # 값 비교
                if matrix[nx][ny] == tmp:
                    stack.append((nx, ny))

        # while문 통과 시, 카운트 + 1
        cnt += 1

    return cnt

# 평범한 사람이 보는 output
result = 0
for x in range(N):
    for y in range(N):
        result += dfs(x, y, N, mat)

# 적록색약 사람이 보는 output
result2 = 0
for x in range(N):
    for y in range(N):
        result2 += dfs(x, y, N, mat_RG)

# 출력
print(result, result2, sep=" ")