import sys
sys.stdin = open("1010.txt")

T = int(input())
for test_count in range(1,T+1):
    N, M = map(int,input().split())

    # 서쪽 N 동쪽 M /// N<=M
    # 순서가 상관없다 => 조합
    # nCr = n!/(n-r)!r!
    # n! 구현하기
    '''
    sum = 1
    for i in range(1,n+1):
        sum *= i
    '''
    # 따라서 M P N 을 구하면 된다.
    # MCN = M! / (M-N)! N!

    # M!를 구하자
    M_sum = 1
    for i in range(1, M+1):
        M_sum *= i

    # N!를 구하자
    N_sum = 1
    for j in range(1, N+1):
        N_sum *= j

    # (M-N)!를 구하자
    M_N_sum = 1
    for t in range(1, M-N+1):
        M_N_sum *= t

    result = M_sum // (M_N_sum * N_sum)

    print(result)

