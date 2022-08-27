# 이진탐색
num = int(input())
for i in range(1, num+1):
    p, a, b = map(int, input().split())
    cnt_a = 0
    cnt_b = 0
    min = 1
    max = p
    while True:
        cnt_a += 1
        c = int((min + max) / 2)
        if c < a:
            min = c
            continue
        elif c > a:
            max = c
            continue
        elif c == a:
            break
    min = 1
    max = p
    while True:
        cnt_b += 1
        c = int((min + max) / 2)
        if c < b:
            min = c
            continue
        elif c > b:
            max = c
            continue
        elif c == b:
            break

    if cnt_a < cnt_b:
        print(f'#{i} A')
    elif cnt_a > cnt_b:
        print(f'#{i} B')
    elif cnt_a == cnt_b:
        print(f'#{i} 0')