# BAEKJOON 2667 - 단지번호붙이기 (S1)

'''
문제
1)

풀이
1)
'''
from pprint import pprint
import sys

sys.stdin = open('B2667.txt')

# input
N = int(input())
mat = [list(map(int, input())) for _ in range(N)]

# delta
dv = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# dfs
def dfs(x, y, N):
    cnt = 0

    if x < 0 or y < 0 or x >= N or y >= N:
        return cnt

    if mat[x][y] == 1:
        mat[x][y] = 0
        stack = [(x, y)]
        while stack:
            v, w = stack.pop()
            cnt += 1
            for i in range(4):
                nv = v + dv[i]
                nw = w + dw[i]

                if nv < 0 or nw < 0 or nv >= N or nw >= N:
                    continue

                if mat[nv][nw] == 1:
                    mat[nv][nw] = 0
                    stack.append((nv, nw))

        return cnt
    return cnt

# output
result = 0
result2 = []
for i in range(N):
    for j in range(N):
        tmp = dfs(i, j, N)
        if tmp != 0:
            result += 1
            result2.append(tmp)
print(result)
result2 = sorted(result2)
for r in result2:
    print(r)