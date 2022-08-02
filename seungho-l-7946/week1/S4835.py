# 구간합
num = int(input())
for i in range(1, num+1):
    n, m = map(int, input().split())
    test_list = list(map(int, input().split()))
    result = []
    for j in range(n - m + 1):
        result.append(sum(test_list[j:j+m]))
    result = sorted(result)
    print(f'#{i} {result[-1]-result[0]}')