# BAEKJOON 17298 - 오큰수 (G4)

'''
문제
1) 크기가 N인 수열 A = A1, A2, ..., AN 이 주어짐.
2) Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미함.
3) 그러한 수가 없는 경우에 오큰수는 -1임.

풀이
1)

입력
1) 첫째 줄에 수열 A의 크기 N이 주어짐.
2) 둘째 줄에 수열 A의 원소 A1, A2, ..., AN이 주어짐.

출력
1) 총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력함.
'''

import sys

sys.stdin = open('B17298.txt')

# input
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * N
for i in range(N - 1, -1, -1):
    if not stack:
        result[i] = -1
        stack.append(numbers[i])
    else:
        while stack:
            if numbers[i] >= stack[-1]:
                stack.pop()
            else:
                result[i] = stack[-1]
                stack.append(numbers[i])
                break
        else:
            result[i] = -1
            stack.append(numbers[i])

result = " ".join(str(s) for s in result)
print(result)

# for i in range(N):
#     for j in range(i + 1, N):
#         if numbers[i] < numbers[j]:
#             stack.append(numbers[j])
#             break
#     else:
#         stack.append(-1)
# result = " ".join(str(s) for s in stack)

# output
# print(result)