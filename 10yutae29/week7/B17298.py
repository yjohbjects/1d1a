# B17298_오큰수

def okensu(n, numbers, ans):
    if len(ans) == 0 or numbers[n] >= ans[n-1] or numbers[n] < numbers[n-1]:
        for i in range(n+1, N):
            if numbers[i] > numbers[n]:
                ans.append(numbers[i])
                break
        else:
            ans.append(-1)
    else:
        ans.append(ans[n-1])
    if n == N-1:
        return ans
    else:
        return okensu(n+1, numbers, ans)



N = int(input())
nums = list(map(int, input().split()))
answer = []
print(okensu(0, nums, answer))





# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[j] > numbers[i]:
#             answer.append(numbers[j])
#             break
#     else:
#         answer.append(-1)
# print(' '.join(map(str,answer)))