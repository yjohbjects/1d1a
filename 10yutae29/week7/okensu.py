import sys
N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
ans = []
n = 0
while n < N:
    if len(ans) == 0 or numbers[n] >= ans[n - 1] or numbers[n] < numbers[n-1]:
        for i in range(n + 1, N):
            if numbers[i] > numbers[n]:
                ans.append(numbers[i])
                break
        else:
            ans.append(-1)
    else:
        ans.append(ans[n - 1])
    n += 1
print(' '.join(map(str, ans)))