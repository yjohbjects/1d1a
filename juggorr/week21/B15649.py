from itertools import permutations
import sys
N, M = map(int, sys.stdin.readline().split())
combs = list(permutations(range(1, N + 1), M))
for comb in combs:
    ans = ''
    for num in comb:
        ans += str(num) + ' '
    print(ans)