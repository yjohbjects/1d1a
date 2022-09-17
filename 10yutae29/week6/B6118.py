# B6118 숨바꼭질

# N: 헛간 갯수, M: 양뱡향 길(간선) 갯수
N, M = map(int,input().split())

# 헛간 정보를 받기 위한 인덱스
hut = [[] for _ in range(N+1)]

# 각 헛간에 연결된 다른 헛간 번호를 입력해줌
for _ in range(M):
    a, b = map(int, input().split())
    hut[a].append(b)
    hut[b].append(a)

# visited 초기화
visited = [0]*(N+1)
# 1번 헛간부터 조사하니 1번 방문설정
visited[1] = 1
queue = [1]

# BFS 탐색
while queue:
    now = queue.pop(0)
    for next_ in hut[now]:
        if visited[next_] == 0:
            # 1번 헛간과의 거리 계산
            visited[next_] = visited[now] + 1
            queue.append(next_)

# 1번헛간으로부터 가장 먼 헛간으로의 거리
hut_max = 0
# 가장 먼 헛간과 같은 거리를 갖는 헛간의 개수
max_count = 0



for idx in range(len(visited)):
    # visited값(1번으로부터 거리)이 hut_max 보다 크다면
    if visited[idx] > hut_max:
        # hut_max를 업데이트
        hut_max = visited[idx]
        # max_count 초기화 (가장 큰 수를 처음 조사했기 때문)
        max_count = 1
        # 최대 거리를 갖는 헛간중 가장 작은 인덱스를 저장
        ans_idx = idx

        # 최대거리를 갖는 다른 헛간을 본다면
    elif visited[idx]==hut_max:
        max_count += 1


print(' '.join(map(str,[ans_idx, hut_max - 1, max_count])))
