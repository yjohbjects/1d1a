import sys
sys.stdin = open('in.txt')

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    arr = list(map(int, sys.stdin.readline().split()))

    # 정류장 갯수    
    N = arr[0]
    
    for i in range(1, N + 1):
        break

# 정류장 이동하면서
# 최적화 문제이기 때문에 dp or greedy로 해결가능
# greedy보단 dp에 가까울듯?
# 어떻게 dp를 활용할 것인가
