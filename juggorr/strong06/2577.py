A = int(input())
B = int(input())
C = int(input())

X = str(A * B * C)

numbers = [0] * 10

for char in X:
    numbers[int(char)] += 1

for number in numbers:
    print(number)