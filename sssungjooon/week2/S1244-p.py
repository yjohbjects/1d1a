import sys
sys.stdin = open("1244.txt")

def change(numbers, cnt):
    global result

    temp = ''
    for number in numbers:
        temp += number
    
    if int(temp) in result[cnt]:
        return
    else:
        result[cnt].append(int(temp))

    if cnt == 0:
        return

    n = len(numbers)

    for i in range(n):
        for j in range(i+1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]

            change(numbers, cnt-1)

            numbers[i], numbers[j] = numbers[j], numbers[i]


# 테스트 케이스 인풋
T = int(input())

for test_count in range(1, T+1):
    temp, cnt = input().split()

    numbers = list(temp)
    result = [[] for _ in range(int(cnt)+1)]

    change(numbers, int(cnt))

    # 이제 답을 출력하자
    print(f'#{test_count} {max(result[0])}')

# 근데 답이 이상하게 출력이 되네..