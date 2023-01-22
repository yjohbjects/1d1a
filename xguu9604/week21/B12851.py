from collections import deque


# def BFS(N, M):
#     global cnt
#     global answer
#     Q = deque()
#     Q.append((N, 0))
#     visited = set()
#     visited.add(N)
#     while Q:
#         now_position, time = Q.popleft()
#         if cnt:
#             if time > answer:
#                 return
#             elif now_position == M:
#                 cnt += 1
#         else:
#             if now_position == M:
#                 cnt += 1
#                 answer = time
#             else:
#                 for i in range(3):
#                     if not i:
#                         if 0 <= now_position * 2 <= 100000:
#                             if now_position * 2 not in visited:
#                                 Q.append((now_position * 2, time + 1))
#                                 visited.add(now_position * 2)
#                             elif now_position * 2 == M:
#                                 Q.append((now_position * 2, time + 1))
#                     elif i == 1:
#                         if 0 <= now_position - 1 <= 100000:
#                             if now_position - 1 not in visited:
#                                 Q.append((now_position - 1, time + 1))
#                                 visited.add(now_position - 1)
#                             elif now_position - 1 == M:
#                                 Q.append((now_position - 1, time + 1))
#                     else:
#                         if 0 <= now_position + 1 <= 100000:
#                             if now_position + 1 not in visited:
#                                 Q.append((now_position + 1, time + 1))
#                                 visited.add(now_position + 1)
#                             elif now_position + 1 == M:
#                                 Q.append((now_position + 1, time + 1))

from collections import deque

'''
visited를 집합으로 사용하면 너무 많은 문제가 생긴다..
그냥 리스트 전부 만들어주고 그 친구를 visited로 사용하는게 제일 무난...?
'''


def BFS(N, M):
    global cnt
    global visited
    Q = deque()
    Q.append(N)
    while Q:
        now = Q.popleft()
        if now == M:
            cnt += 1

        else:
            for i in [now + 1, now - 1, now * 2]:
                if 0 <= i <= 100000:
                    if not visited[i] or visited[i] >= visited[now] + 1:
                        Q.append(i)
                        visited[i] = visited[now] + 1


N, M = map(int, input().split())
cnt = 0
visited = [0] * 100001
if N == M:
    cnt = 1
else:
    BFS(N, M)

print(visited[M])
print(cnt)
