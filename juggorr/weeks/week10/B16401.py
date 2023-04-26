# 이진 탐색을 위해 구해야 할 것
# l, r
# 가운데 값이 어떤 조건을 만족하지 못하면 새로운 r or l로 설정하고
# 어떤 조건을 만족하면 새로운 l or r로 설정하는지
# 반복문 종료조건? 을 설정하는게 핵심


N, M = map(int, input().split())
cookies = list(map(int, input().split()))
l = max(cookies) // N
r = max(cookies)
ans = 0

while l <= r:
    c = (l + r) // 2
    cnt = 0
    flag = True
    # 이 반복문을 여러번 돌려서 값을 계속 빼주면서
    # count를 올려줘야 하는데
    # 어떤식으로 해야하지?
    for cookie in cookies:
        
        while cookie >= c:
            cookie -= c
            cnt += 1
        
            if cnt == N:
                ans = c
                l = c + 1
                flag = False
                break
        if not flag:
            break

    if cnt < N:
        r = c - 1

print(ans)