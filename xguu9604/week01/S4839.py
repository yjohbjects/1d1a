T = int(input())
cnt = 1
while T > 0:
    P, Pa, Pb = map(int,input().split(" "))
    l = 1
    r = P
    cnt_A = 0
    cnt_B = 0
    c = 0                          # 이진 탐색을 통해 계산될 값을 담을 변수
    while c != Pa:
        c = int((l+r)/2)
        if c < Pa:
            l = c
        else:
            r = c
        cnt_A += 1
    c = 0
    l = 1
    r = P
    while c != Pb:
        c = int((l+r)/2)
        if c < Pb:
            l = c
        else:
            r = c
        cnt_B += 1

    if cnt_A < cnt_B:
        print(f'#{cnt} A')
    elif cnt_A > cnt_B:
        print(f'#{cnt} B')
    else:
        print(f'#{cnt} 0')
    cnt += 1
    T -= 1



