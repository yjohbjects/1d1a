T = int(input())
cnt = 1

while T > 0:
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    result = 0
    for i in range(0, M-N+1):       # 여기서 문제가 생겼었음 & if ~ in ~: 가 메모리 초과 발생
        if str1 == str2[i:i+N]:
            result = 1
        else:
            pass

    print(f'#{cnt} {result}') 

    cnt += 1
    T -= 1
    