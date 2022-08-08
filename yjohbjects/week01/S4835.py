test_case = int(input())
x = 0
while x < test_case:
    n, m = map(int, input().split())
    number_list = list(map(int, input().split()))

    minimum = 20000000000
    maximum = 0

    for i in range(n-m+1):
        if minimum > sum(number_list[i:i+m]):
            minimum = sum(number_list[i:i+m])

        if maximum < sum(number_list[i:i+m]):
            maximum = sum(number_list[i:i+m])
    
    print(f'#{x + 1} {maximum, minimum, maximum-minimum}')
    x += 1
