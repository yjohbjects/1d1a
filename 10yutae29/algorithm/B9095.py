# B9095_1, 2, 3 더하기

T = int(input())

dp = [1, 1, 2, 4]

for i in range(4,12):
    dp.append(sum(dp[i-3:i]))

for _ in range(T):
    print(dp[int(input())])

