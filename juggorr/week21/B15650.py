from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().split())
combs = list(combinations(range(1, N + 1), M))
for comb in combs:
    ans = ''
    for num in comb:
        ans += str(num) + ' '
    print(ans)