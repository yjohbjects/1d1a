# B1240_노드사이의 거리

N, M = map(int,input().split())

edge_distance = [[] for _ in range(N+1)]
for n in range(N-1):
    from_node, to_node, distance = map(int,input().split())
    edge_distance[from_node].append([to_node, distance])
    edge_distance[to_node].append([from_node, distance])


edge_know = []
for m in range(M):
    start, end = map(int,input().split())

    queue = [start]
    visited = [0] * (N+1)
    visited[start] = 1
    next_node = start
    while next_node != end:
        now = queue.pop(0)
        for next_info in edge_distance[now]:
            next_node, next_distance = next_info

            if not visited[next_node]:
                visited[next_node] = visited[now] + next_distance
                queue.append(next_node)
                if next_node == end:
                    break
    print(visited[end]-1)



