import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
ns = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().split()))

ns_sorted = sorted(ns)
# print(ns_sorted)


# 처음에 들어오는 배열을 2차원으로 바꿔주기
# 마지막 경우에 어떻게 할 것 인지?
ns_real = []
tmp = ns_sorted[0]
n_count = 1
for i in range(1, N):

    # 같은 숫자가 나왔다면
    if tmp == ns_sorted[i]:
        n_count += 1

        # 마지막이라면?
        if i == N - 1:
            ns_real.append([tmp, n_count])

    # 다른 숫자가 나왔다면
    else:
        ns_real.append([tmp, n_count])
        tmp = ns_sorted[i]
        n_count = 1
        
        # 마지막일 경우 분기처리
        if i == N - 1:
            ns_real.append([tmp, 1])

# print(ns_real)

result = ''
# ms 리스트를 순회하면서 몇개 인지 찾아보자 구~~~
flag = True
for m in ms:
    
    l, r = 0, len(ns_real) - 1

    while l <= r:
        
        c = (l + r) // 2

        if ns_real[c][0] > m:
            r = c - 1

        elif ns_real[c][0] < m:
            l = c + 1

        elif ns_real[c][0] == m:
            result += f'{ns_real[c][1]} '
            flag = False
            break
    
    if flag:
        result += '0 '

    flag = True

print(result)