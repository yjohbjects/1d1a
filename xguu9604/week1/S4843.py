T = int(input())
cnt = 1
while T > 0:
    N = int(input())
    lst = input().split()     # split(' ')로 하면 런타임에러..--> .split()과 같이 조건을 안주면 잘만 풀림 ...
    lst = list(map(int,lst))
    result = []

    while len(result) < 10:
        max_num = max(lst)
        min_num = min(lst)
        result.append(max_num)
        result.append(min_num)
        lst.remove(max_num)
        lst.remove(min_num)

    result = map(str,result)
    final = ' '.join(result)
    print(f'#{cnt} {final}')
    cnt += 1
    T -= 1
