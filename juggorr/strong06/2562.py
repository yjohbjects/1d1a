import sys
sys.stdin = open('in.txt')

numbers = [int(sys.stdin.readline()) for _ in range(9)]

max_num = 0
max_num_idx = 0

for i in range(9):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_num_idx = i + 1

print(max_num)
print(max_num_idx)