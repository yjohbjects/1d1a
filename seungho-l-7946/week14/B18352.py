# BAEKJOON 18352 - 특정 거리의 도시 찾기 (S2)

'''
문제
1) 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
2) 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램

풀이
1) 거리가 1이라 BFS가 아니면 못풀듯 싶습니다.
2) 다익이 쓰면 메모리초과, readline을 쓰지 않으면 시간 초과가 발생하네요.
3) shit the fuxkin condition

입력
1) 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
2) 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
3) 이는, A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다.

출력
1) X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
2) 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력
'''

from collections import deque
import sys

sys.stdin = open('B18352.txt')

# input
N, M, K, X = map(int, sys.stdin.readline().split())
mat = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    mat[x].append(y)

def BFS(start, matrix, distance):
    q = deque([start])
    distance[start] = -1
    while q:
        v = q.popleft()
        for w in matrix[v]:
            if not distance[w]:
                if distance[v] == -1:
                    distance[w] = distance[v] + 2
                    q.append(w)
                else:
                    distance[w] = distance[v] + 1
                    q.append(w)

result = -1
D = [0] * (N + 1)
BFS(X, mat, D)

for x in range(N + 1):
    if D[x] == K:
        result += 1
        print(x)

# output
if result == (-1):
    print(result)