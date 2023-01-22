# B11399 ATM
# https://www.acmicpc.net/problem/11399

N = int(input())
time_cost = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
    if not i :
        answer[i] = min(time_cost)
    else:
        answer[i] = answer[i-1] + min(time_cost)
    time_cost[time_cost.index(min(time_cost))] = 1001

print(sum(answer))