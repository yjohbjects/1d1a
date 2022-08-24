N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers = sorted(numbers, key=len)
print(numbers)
# print(*numbers, sep='\n')