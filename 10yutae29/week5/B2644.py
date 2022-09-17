# B2644 촌수계산

n = int(input())  # 사람 수
s, e = map(int, input().split())  # 시작촌수, 끝나는 촌수

m = int(input())  # 부모 자식들 간의 관계의 개수

chon_list = [[] for _ in range(n+1)]

for k in range(m):
    a, b = map(int, input().split())
    chon_list[a].append(b)
    chon_list[b].append(a)

visited = [0]*(n+1)
visited[s] = 1  # 시작 인덱스 방문 표시
stack = [s]     # 스택에 시작 인덱스 푸쉬
now = s         # 현재 확인하고 있는 인덱스를 담는 변수 now
c_count = 0     # 촌수를 더해주기 위한 변수
flag = 0        # 촌수 계산 가능여부를 판별해주는 변수 flag

while stack:
    for next in chon_list[now]:     # 현재 확인하고 있는 인덱스(now)에 연결된 인덱스(next) 탐색
        if visited[next] == 0:
            stack.append(next)
            now = next              # 다음 인덱스로 이동
            visited[now] = 1        # 방문 표시
            c_count += 1            # 촌수 계산 + 1
            break
    else:                           # 만약 now에 연결된 next 중 방문안한 곳이 없다면
        stack.pop()                 # 스택의 탑 제거
        if len(stack) != 0:         # 만약 스택이 비어있지 않다면
            now = stack[-1]         # now = 스택의 탑
                                    # 즉, 이전 인덱스로 올라감
        c_count -= 1                # 다시 돌아가므로 촌수 계산 -1
    if now == e:                    # 만약 now = end 라면
        flag = 1                    # 촌수 계산 가능하단걸 표시
        break

if flag:                # 촌수 계산이 가능하면
    print(c_count)      # c_count를 출력
else:                   # 촌수 계산이 불가능하면
    print(-1)           # -1을 출력