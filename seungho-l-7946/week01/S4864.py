num = int(input())

for i in range(1, num+1):
    test = input()
    comparison = input()
    if test in comparison:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')