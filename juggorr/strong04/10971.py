import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())

costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 갱신할 최소비용
min_cost = N * 1000000
# 방문표시
visited = [0] * N
# 방문순서 (도시가 0번부터기 때문에 -1로 배열채우기)
order = [-1] * N

# print(min_cost)
# 모든 경우의 수 = N!
# 모든 가짓수를 만들면서 최소비용을 넘은 경우 종료
# 최종장에 도달해서 최소비용보다 작으면 갱신
cost = 0

def getMinCost(cnt):
    global cost, min_cost

    # 최소비용보다 비용이 큰 시점에서 바로 종료
    if cost > min_cost:
        return

    # 모든 도시를 순회한 후 최소비용보다 작다면 갱신
    if cnt == N:
        # 최종 방문한 도시에서 출발한 도시로 갈 수 있다면
        if costs[order[N - 1]][order[0]] != 0:
            cost += costs[order[N - 1]][order[0]]
            min_cost = min(cost, min_cost)
            cost -= costs[order[N - 1]][order[0]]
        return
    
    # 도시를 순회하면서 비용구하기
    for i in range(N):
        # 순회를 시작하는 시점과 순회중인 시점을 나누어야 함
        if cnt == 0:
            visited[i] = 1
            order[cnt] = i
            getMinCost(cnt + 1)
            visited[i] = 0
            order[cnt] = -1
        else:
            # 방문한 적이 없고 / 방문할 수 있는 도시라면
            if not visited[i] and costs[order[cnt - 1]][i] != 0:
                # 방문표시하고
                visited[i] = 1
                # 순서에 넣기
                order[cnt] = i
                # 비용에 더하기
                cost += costs[order[cnt -1]][i]
                getMinCost(cnt + 1)
                # 이하 백트래킹
                visited[i] = 0
                order[cnt] = -1
                cost -= costs[order[cnt -1]][i]

getMinCost(0)
print(min_cost)