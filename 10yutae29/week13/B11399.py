# B11399_ATM

# 사람의 수
N = int(input())

# 각 사람이 돈을 인출하는데 걸리는 시간
times = list(map(int, input().split()))
# 인출하는데 걸리는시간이 적은사람이 먼저 인출해야함
times.sort()

# 총 걸리는 시간을 저장할 answer
answer = 0

# 첫번째 사람이 인출하는데 걸리는 시간은
# 총 N명의 사람이 겪음
# n번째 사람이 인출하는데 걸리는 시간은
# 총 N-n+1명의 사람이 겪음
for i in range(N):
    answer += times[i]*(N-i)
print(answer)