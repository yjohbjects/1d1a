# BAEKJOON 1012 - 유기농 배추 (S2)

'''
문제
1) 2차원 배열로 배추의 좌표가 주어진다.
2) 크게 배추무리의 덩어리가 몇 개가 있는지 세는 문제이다.

풀이 : DFS에서 Boolean형을 return하도록 설계
1) 반복문
2) 재귀 - RunTime;;
'''
from pprint import pprint
import sys

sys.stdin = open('B1012.txt')

# delta
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, R, C):

    # 매트릭스 바깥일 경우
    if x < 0 or y < 0 or x >= R or y >= C:
        return False

    # 배추가 있을 경우
    if cabbage[x][y] == 1:

        # 배추 뽑아버림
        cabbage[x][y] = 0

        # 깊이 탐색용 stack 선언
        stack = [(x, y)]
        while stack:

            # 좌표 초기화
            x, y = stack.pop()

            # 상하좌우 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 좌표 바깥 건너뛰기
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue

                # 배추 있을 경우 뽑고 스택처리
                if cabbage[nx][ny] == 1:
                    cabbage[nx][ny] = 0
                    stack.append((nx, ny))
        # 배추 무리를 소탕하고 나면 True 반환 및 종료
        return True

    # 배추 없을경우 바로 False 반환
    return False

T = int(input())

for tc in range(T):

    # input
    R, C, K = map(int, input().split())
    cabbage = [[0] * C for _ in range(R)]

    # 배추 심기
    for k in range(K):
        i, j = map(int, input().split())
        cabbage[i][j] += 1

    # output
    result = 0
    for i in range(R):
        for j in range(C):
            if dfs(i, j, R, C) == True:
                result += 1
    print(result)


# def dfs(x, y):
#     if x < 0 or y < 0 or x >= R or y >= C:
#         return False
#
#     if cabbage[x][y] == 1:
#         cabbage[x][y] = 0
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         return True
#
#     return False
#
# T = int(input())
#
# for tc in range(T):
#
#     # input
#     R, C, K = map(int, input().split())
#     cabbage = [[0] * C for _ in range(R)]
#
#     for k in range(K):
#         i, j = map(int, input().split())
#         cabbage[i][j] += 1
#
#     # output
#     result = 0
#     for i in range(R):
#         for j in range(C):
#             if dfs(i, j) == True:
#                 result += 1
#     print(result)