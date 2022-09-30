# BAEKJOON 1260 - DFS와 BFS (S2)

'''
문제
1) 1번부터 N번까지 N개의 정점을 BFS, DFS 두 개의 탐색 결과를 출력하는 프로그램을 작성
2) 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은 것을 우선시
3) 더 이상 방문할 정점이 없는 경우 종료

입력
1) 정점의 수 N, 간선의 수 M, 탐색 시작 정점 번호 V
2) 다음 M개의 연결된 양방향 간선 정보 (중복 가능)

출력
1) 첫째 줄에 DFS 결과, 다음 줄에 BFS 결과를 출력
2) 결과는 V부터 방문된 점을 순서대로 출력

풀이
1) BFS, DFS 작성
'''

from pprint import pprint
from collections import deque
import sys

sys.stdin = open('B1260.txt')

def DFS(start):
    stack = []
    stack.append(start)
    D_visit[start - 1] = 1
    print(start, end=' ')
    while stack:
        top = stack[-1]
        for next_idx in range(N):
            if mat[top - 1][next_idx] == 1 and D_visit[next_idx] == 0:
                stack.append(next_idx + 1)
                D_visit[next_idx] = 1
                print(next_idx + 1, end=' ')
                break
        else:
            stack.pop()

def BFS(start):
    queue = deque()
    queue.append(start)
    B_visit[start - 1] = 1
    while queue:
        last = queue.popleft()
        print(last, end=' ')
        for next_idx in range(N):
            if mat[last - 1][next_idx] == 1 and B_visit[next_idx] == 0:
                queue.append(next_idx + 1)
                B_visit[next_idx] = 1

# input
N, M, V = map(int, input().split())
mat = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    mat[x - 1][y - 1] = 1
    mat[y - 1][x - 1] = 1

# visit
D_visit = [0 for _ in range(N)]
B_visit = [0 for _ in range(N)]

# output
DFS(V)
print()
BFS(V)