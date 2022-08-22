# S5102 노드의 거리


def BFS(G, s, e, n):  # 그래프 G, 탐색 시작점 s, 도착점 e
    visited = [0]*(n+1)  # n: node_num 정점의 개수
    queue = []  # 큐 생성
    queue.append(s)  # 시작점 v를 큐에 삽입 s: start
    num_count = 0
    stair = queue[::]  # 한 층에 있는 노드
    while queue:
        t = queue.pop(0)  # 큐의 첫번쨰 원소
        if t == e:
            return num_count   # 여기에 간선 갯수 리턴해야함
        if not visited[t]:  # 방문되지 않은 곳이라면
            visited[t] = True  # 방문한 것으로 표시
        for i in G[t]:  # t와 연결된 모든 선에 대해
            if not visited[i]:  # 방문되지 않은 곳이라면
                queue.append(i)  # 큐에 넣기
        floar_check = 0
        for k in stair:
            if k in queue:
                floar_check += 1
        if floar_check == 0:
            num_count += 1
            stair = queue[::]  # 한 층에 있는 노드

    return 0

T = int(input())

for t in range(1, T+1):
    node_num, ganseon_num = list(map(int, input().split()))
    ganseon_list = [[] for _ in range(node_num + 1)]
    for ganseon in range(ganseon_num):
        a, b = map(int, input().split())
        ganseon_list[a].append(b)
        ganseon_list[b].append(a)
    start, end = list(map(int, input().split()))

    print(f'#{t} {BFS(ganseon_list,start,end,node_num)}')