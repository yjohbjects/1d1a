# B17298 오큰수

N = int(input())

nums = list(map(int, input().split()))
answer = []
for i in range(N):
    k = nums[i]
    for j in range(i, N):
        h = nums[j]
        if k < h:
            answer.append(str(h))
            break
    else:
        answer.append('-1')
print(' '.join(answer))
