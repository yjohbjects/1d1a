# S4869_종이붙이기_재귀
import time
import sys
sys.stdin = open('input.txt')

start = time.time()

def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-2) + 2**(n-1)

T = int(input())
for t in range(1,T+1):

    N = int(input())//10
    print(f'#{t} {paper(N)}')

print('Time : {}초'.format(time.time() - start))