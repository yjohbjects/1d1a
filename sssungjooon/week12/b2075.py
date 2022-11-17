# 첫째 줄에 N이 주어진다.
N = int(input())

# 배열 없이도 그냥 넣어보자
numbers = []
for line in range(N):
    number = list(map(int,input().split()))
    for n in number :
        numbers.append(n)

new_numbers = sorted(numbers,reverse=True)

print(new_numbers[N-1])
