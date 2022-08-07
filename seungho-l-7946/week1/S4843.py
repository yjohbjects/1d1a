num = int(input())

for i in range(1, num+1):
    n = int(input())
    test_list = list(map(int, input().split()))
    test_list = sorted(test_list)
    result = []
    while len(result) != 10:
        result.append(test_list[-1])
        test_list.pop()
        test_list = test_list[::-1]
    result = ' '.join(map(str, result))
    print(f'#{i} {result}')