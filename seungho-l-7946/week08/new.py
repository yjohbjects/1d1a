# B1966 프린터 큐

from collections import deque
import sys
sys.stdin = open('B1966.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = deque(list(map(int, input().split())))

    # by priority
    priority = sorted(nums, reverse=True)

    i = 0
    cnt = 0
    pin = 0
    while nums:
        # if priority
        if nums[0] == priority[pin]:
            if i == M:
                cnt += 1
                break
            pin += 1
            nums.popleft()
            N -= 1
            cnt += 1

        # if not priority
        else:
            nums.rotate(-1)
        i = (i + 1) % N

    print(cnt)