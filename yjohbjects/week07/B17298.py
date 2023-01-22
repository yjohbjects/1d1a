# B17298 오큰수

# [3, 5, 2, 7]

N = int(input())
nums = list(map(int, input().split()))
answer = [0] * N
stack = []

for i in range(N-1, -1, -1):
    # 제일 끝 숫자는 -1를 저장하고, stack에 숫자 저장
    if not stack:
        answer[i] = -1
        stack.append(nums[i])

    else:
        while stack:

            # 오큰수를 만날 경우
            if nums[i] < stack[-1]:
                answer[i] = stack[-1]
                stack.append(nums[i])
                break

            # 작은 숫자를 만날 경우
            elif nums[i] >= stack[-1]:
                stack.pop()
        
        # 아무 숫자도 못 만날 경우
        else:
            answer[i] = -1
            stack.append(nums[i])

print(*answer)
