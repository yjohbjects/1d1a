# BAEKJOON 1916 - 최소비용 구하기 (G5)

'''
문제
1) N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
2) 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
3) A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

풀이
1)

입력
1) 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다.
2) 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다.
3) 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다.
4) 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
5) 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
6) 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

출력
1) 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
'''

import sys

sys.stdin = open('B1916.txt')

# input
N = int(input())

INF = 999999
mat = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(int(input())):
    s, e, d = map(int, input().split())
    mat[s][e] = d

start, end = map(int, input().split())

distance = [0] * (N + 1)

def dijkstra(start, N, matrix, distance):

    U = [0] * (N + 1)
    U[start] = 1
    for v in range(N + 1):
        distance[v] = matrix[start][v]

    for _ in range(N):
        minV = INF
        w = 0
        for i in range(N + 1):
            if U[i] == 0 and minV > distance[i]:
                minV = distance[i]
                w = i
        U[w] = 1

        for v in range(N + 1):
            if 0 <= matrix[w][v] < INF:
                distance[v] = min(distance[v], distance[w] + matrix[w][v])

dijkstra(start, N, mat, distance)

result = distance[end]

# output
print(result)