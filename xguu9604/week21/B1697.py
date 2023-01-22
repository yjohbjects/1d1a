from collections import deque

'''
BFS를 이용한 풀이
visited 사용은 언제나 중요한것
'''


def BFS(N, M):
    global answer
    Q = deque()
    Q.append((N, 0))
    # visited 를 집합으로 계산해주기
    visited = set()
    visited.add(N)
    while Q:
        now_position, time = Q.popleft()
        # BFS로 움직이는 친구기때문에 제일 먼저 만나는 답이 최소시간일 수 밖에 없음
        if now_position == M:
            answer = min(answer, time)
            # 리턴해도 무방
            return

        else:
            for i in range(3):
                if not i:
                    # 다음 이동값이 범위내에 있고 아직 방문한 노드가 아닐 경우에 Q에 추가하고 방문표시까지
                    if now_position * 2 <= 100000 and now_position * 2 not in visited:
                        Q.append((now_position * 2, time + 1))
                        visited.add(now_position * 2)
                elif i == 1:
                    if now_position - 1 >= 0 and now_position - 1 not in visited:
                        Q.append((now_position - 1, time + 1))
                        visited.add(now_position - 1)
                else:
                    if now_position + 1 <= 100000 and now_position + 1 not in visited:
                        Q.append((now_position + 1, time + 1))
                        visited.add(now_position + 1)


N, M = map(int, input().split())
answer = float('inf')
BFS(N, M)

print(answer)
