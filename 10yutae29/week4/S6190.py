# S1860 진기의 최고급 붕어빵
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc&categoryId=AV5LsaaqDzYDFAXc&categoryType=CODE&problemTitle=1860&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

# 진기 뒤졌다 진짜



T = int(input())

for t in range(1, T+1):
    p_num, b_time, b_num = map(int, input().split())
    # 사람 수, 붕어빵 제조 시간, 한번에 나오는 붕어빵 갯수

    p_times = list(map(int, input().split()))
    #  사람별 도착시간

    time = 0
    boong = []
    flag = 0
    while time <= max(p_times):


        if time % b_time == 0 and time != 0:
            for _ in range(b_num):
                boong.append(1)

        for p_time in p_times:
            if p_time == time and len(boong) > 0:
                boong.pop()
            elif p_time == time and len(boong) == 0:
                flag = 1
                break
        if flag == 1:
            break
        time += 1

    if flag == 1:
        print(f'#{t} Impossible')
    else:
        print(f'#{t} Possible')


