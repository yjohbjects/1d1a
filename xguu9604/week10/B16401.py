import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
cookies = list(map(int, input().split()))
left = 1
right = max(cookies)
max_cookie = 0
while True:
    mid = (left + right) // 2
    cnt = 0
    for cookie in cookies:
        cnt += cookie // mid
    if cnt >= M:
        left = mid + 1
        max_cookie = mid
    elif cnt < M:
        right = mid - 1
    if left > right:
        break
print(max_cookie)