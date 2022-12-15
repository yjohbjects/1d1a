# B3085 사탕 게임

N = int(input())

candies = [list(input()) for _ in range(N)]
print(candies)

for i in range(N):
    for j in range(N):
        if j > 0 and candies[i][j] == candies[i][j-1]:
            pass
