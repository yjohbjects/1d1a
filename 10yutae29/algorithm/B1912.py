# B1912_연속합

n = int(input())

nums = list(map(int,input().split()))

# 이전 인덱스까지의 합이 음수라면 더할 필요가 없다
for z in range(1,n):
    if nums[z-1] > 0:
        nums[z] += nums[z-1]
print(max(nums))

# arr = [[0] * n for _ in range(n)]
#
# ans = -(10**4)
#
# for i in range(n):
#     arr[i][i] = nums[i]
#     ans = max(ans, arr[i][i])
#
#     for j in range(i+1,n):
#         arr[i][j] = arr[i][j-1] + nums[j]
#         ans = max(ans, arr[i][j])
# print(ans)
#
# dp = [nums[0]]
#
# ans2 = -100000
#
# for k in range(1,n):
#     dp.append(dp[k-1]+nums[k])
#
# minus = 0
# for z in range(n):
#     ans2 = max(ans2, max(dp[z::])-minus)
#     minus += nums[z]
#
# print(ans2)