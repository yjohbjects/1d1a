# Bakjoon 10090 - Counting Inversions

N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
# for i in range(N):
#     if numbers[i] == max(numbers):
#         cnt += N - 1 - i
#         continue
#     elif numbers[i] == min(numbers):
#         continue
#     cnt_up = 0
#     cnt_down = 0
#     for j in range(i+1, N):
#         if numbers[i] > numbers[j]:
#             cnt += 1
#             cnt_down += 1
#             if cnt_down == numbers[i] - min(numbers[i+1:]):
#                 break
#         else:
#             cnt_up += 1
#             if cnt_up == max(numbers[i+1:]) - numbers[i]:
#                 cnt += N - i - 1 - cnt_up - cnt_down
#                 break
# print(cnt)
s_numbers = sorted(numbers)

for i in range(N):
    if numbers[i] == s_numbers[-1]:
        cnt += N - 1 - i
        continue
    elif numbers[i] == s_numbers[0]:
        continue
    cnt_up = 0
    cnt_down = 0
    for j in range(i+1, N):
        if numbers[i] < numbers[-1]:
            if numbers[i] < numbers[j]:
                continue
            else:
                cnt += 1
                cnt_down += 1
                if cnt_down == numbers[i] - min(numbers[i+1:]):
                    break
        else:
            if numbers[i] > numbers[j]:
                if i == (N - 2):
                    cnt += 1
                continue
            else:
                cnt_up += 1
                if cnt_up == max(numbers[i+1:]) - numbers[i]:
                    cnt += N - i - 1 - cnt_up - cnt_down
                    break
print(cnt)