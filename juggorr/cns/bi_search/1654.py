# 이분탐색에서 중요한것
# 1. 최소값 최대값 설정 OjO
# 최초에는 (최대길이 // N ~ 총합길이 // M)
# 이렇게하면 뭔가 안됨 이유는 조금더 알아봐야함
# => 1부터 최대길이로 하니깐 딱됨
# 
# 2. 종료조건
# 처음에는 N이 달성되면 종료 => 말도안됨...
# 이분탐색의 기초 종료조건
# => 왼쪽 끝이 오른쪽 끝보다 커지면 종료(더 이상 탐색불가)


import sys
sys.stdin = open('in.txt')

K, N = map(int, sys.stdin.readline().split())

lines = [int(sys.stdin.readline()) for _ in range(K)]

def bi_search(l, r):

    while l <= r:
         
        c = (l + r) // 2
        counts = 0

        for line in lines:
            counts += line // c

        if counts >= N:
            l = c + 1

        else:
            r = c - 1

        print(l, r, c)
    
    return r

print(bi_search(1, max(lines)))