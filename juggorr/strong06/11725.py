import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
# 연결 정보 표시할 리스트 만들기 
# 무식하게 다 표시하는게아니라 연결정보만가지고 표시하면됨 ㅅㅂ..
maap = [[] for _ in range(N + 1)]
# 지도에 표시하기
for _ in range(N - 1):
    i, j = map(int, sys.stdin.readline().split())
    maap[i].append(j)
    maap[j].append(i)

# 방문표시
visited = [0] * (N + 1)

# 깊이우선탐색하면서 방문표시하기?
def DFS():
    stack = [1]
    visited[1] = 1

    while stack:
        i = stack.pop()

        for j in maap[i]:
            # 연결되어있고 방문한 적이 없다면
            if not visited[j]:
                # 스택에넣고
                stack.append(j)
                # 방문표시
                visited[j] = i
DFS()

for i in range(2, N + 1):
    print(visited[i])