# S4869_종이붙이기_Memoization
import time
import sys
sys.stdin = open('input.txt')

start = time.time()

def memo(n):
    global nums
    if n >= 2 and len(nums) <= n:
        memo(n-1)
        nums.append(memo(n-2) + 2**(n-1))
    return nums[n]

T = int(input())
for t in range(1, T+1):
    N = int(input())//10
    nums = [0, 1, 3]
    print(f'#{t} {memo(N)}')

print('Time : {}초'.format(time.time() - start))