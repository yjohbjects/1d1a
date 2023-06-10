import sys
sys.setrecursionlimit(100000)
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 갱신하기 위한 여행의 최소비용 설정
min_cost = 0
for i in range(N):
    min_cost += sum(W[i])

# 핵심은 W[i][j]와 W[j][i]가 다른경우
# 고려할 필요가 있음? 어차피 다 세는건데
def TSP(town):
    global total_cost

    # 모든 도시를 순회했을 경우
    if sum(is_visited) == N:
        # 비용이 최소값 보다 작다면 갱신
        min_cost = min(min_cost, total_cost)
        return

    # 도시들을 순회하면서
    for i in range(N):
        # 자기 자신이 아니고, 이동할 수 있다면
        if i != town and W[town][i]:
            is_visited[i] = 1
            total_cost += W[town][i]
            TSP(i)
            is_visited[i] = 0
            total_cost -= W[town][i]


for i in range(N):
    print(i)
    # 순회비용
    total_cost = 0
    is_visited = [0] * N
    TSP(i)

print('정답')
print(min_cost)