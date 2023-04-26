import sys
sys.stdin = open('5097.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    print(f'#{tc + 1} {lst[M % N]}')