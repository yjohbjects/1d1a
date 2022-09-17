# S4869_종이붙이기_tobulation
import time
import sys
sys.stdin = open('input.txt')

start = time.time()

T = int(input())

for t in range(1,T+1):
    N = int(input())//10
    f = [1, 3]
    for i in range(2,N):
        f.append(f[i-2] + 2**i)

    print(f'#{t} {f.pop()}')

print('Time : {}초'.format(time.time() - start))
