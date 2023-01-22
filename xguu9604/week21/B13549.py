from collections import deque


# def BFS(N, M):
#     global visited
#     Q = deque()
#     Q.append(N)
#     while Q:
#         now = Q.popleft()
#         if now == M:
#             continue
#         else:
#             if not visited[M]:
#                 for i in range(3):
#                     if not i:
#                         if now + 1 <= 100000:
#                             if not visited[now + 1] or visited[now + 1] >= visited[now] + 1:
#                                 Q.append(now + 1)
#                                 visited[now + 1] = visited[now] + 1
#                     elif i == 1:
#                         if 0 <= now - 1:
#                             if not visited[now - 1] or visited[now - 1] >= visited[now] + 1:
#                                 Q.append(now - 1)
#                                 visited[now - 1] = visited[now] + 1
#                     else:
#                         if now * 2 <= 100000:
#                             if not visited[now * 2] or visited[now * 2] >= visited[now]:
#                                 Q.append(now * 2)
#                                 visited[now * 2] = visited[now]


def BFS(N, M):
    global cnt
    global answer
    tmp = float('inf')
    Q = deque()
    Q.append((N, 0, 0))
    visited = set()
    visited.add(N)
    while Q:
        now_position, time, teleported = Q.popleft()
        if cnt:
            if time > answer:
                break
            elif now_position == M:
                tmp = min(tmp, time - teleported)
        else:
            if now_position == M:
                cnt += 1
                answer = time
            else:
                for i in range(3):
                    if not i:
                        if 0 <= now_position * 2 <= 100000:
                            if now_position * 2 not in visited:
                                Q.append((now_position * 2, time + 1, teleported + 1))
                                visited.add(now_position * 2)
                            elif now_position * 2 == M:
                                Q.append((now_position * 2, time + 1, teleported + 1))
                    elif i == 1:
                        if 0 <= now_position - 1 <= 100000:
                            if now_position - 1 not in visited:
                                Q.append((now_position - 1, time + 1, teleported))
                                visited.add(now_position - 1)
                            elif now_position - 1 == M:
                                Q.append((now_position - 1, time + 1, teleported))
                    else:
                        if 0 <= now_position + 1 <= 100000:
                            if now_position + 1 not in visited:
                                Q.append((now_position + 1, time + 1, teleported))
                                visited.add(now_position + 1)
                            elif now_position + 1 == M:
                                Q.append((now_position + 1, time + 1, teleported))
    return tmp


N, M = map(int, input().split())
answer = float('inf')
cnt = 0
if N == M:
    print(0)
else:
    times = BFS(N, M)
    print(times)