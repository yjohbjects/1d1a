import sys
sys.stdin = open('input.txt')


def eat_candies_row(lst, num):
    global max_candies
    for row in range(num):
        can_eat = 1
        for col in range(num - 1):
            if lst[row][col] == lst[row][col + 1]:
                can_eat += 1
            else:
                if can_eat > max_candies:
                    max_candies = can_eat
                can_eat = 1
        if can_eat > max_candies:
            max_candies = can_eat


def eat_candies_col(lst, num):
    global max_candies
    for col in range(num):
        can_eat = 1
        for row in range(num - 1):
            if lst[row][col] == lst[row + 1][col]:
                can_eat += 1
            else:
                if can_eat > max_candies:
                    max_candies = can_eat
                can_eat = 1
        if can_eat > max_candies:
            max_candies = can_eat


N = int(input())
candies = [list(map(str, input())) for _ in range(N)]
max_candies = 0

for i in range(N-1):
    for j in range(N):
        if candies[i][j] != candies[i + 1][j]:
            candies[i][j], candies[i + 1][j] = candies[i + 1][j], candies[i][j]
            eat_candies_row(candies, N)
            eat_candies_col(candies, N)
            candies[i][j], candies[i + 1][j] = candies[i + 1][j], candies[i][j]

for j in range(N-1):
    for i in range(N):
        if candies[i][j] != candies[i][j + 1]:
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
            eat_candies_row(candies, N)
            eat_candies_col(candies, N)
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]

print(max_candies)
