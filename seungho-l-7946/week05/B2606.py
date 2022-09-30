# BAEKJOON 2606 - 바이러스 (S3)

'''
문제
1) 간선으로 연결되면 모두 바이러스가 걸린다.
2) 추가적으로 걸리는 컴퓨터의 수를 출력하시오.

풀이
1) visited가 추가될 때 count를 한다.
'''
from pprint import pprint
import sys

sys.stdin = open('B2606.txt')

# input
V = int(input())
E = int(input())
adjList = [list(map(int, input().split())) for _ in range(E)]
mat = [[0] * (V + 1) for _ in range(V + 1)]
for adj in adjList:
    mat[adj[0]][adj[1]] += 1
    mat[adj[1]][adj[0]] += 1

def dfs(s):
    visited = [0] * (V + 1)
    cnt = 0
    visited[s] = 1
    stack = [s]
    while stack:
        x = stack.pop()
        for y in range(V + 1):
            if mat[x][y] == 1 and visited[y] == 0:
                stack.append(y)
                visited[y] = 1
                cnt += 1
    return cnt

# output
result = dfs(1)
print(result)