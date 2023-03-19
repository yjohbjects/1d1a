# B2096_내려가기

N = int(input())

game = []

for _ in range(N):
    game.append(list(map(int,input().split())))

# 문제에 할당된 메모리가 적다
# 두줄짜리 dp 배열을 만든 후 데이터를 읽고 읽은 데이터는 버리는 방식으로 한다
dp_max = [game[0][:],[0,0,0]]
dp_min = [game[0][:],[0,0,0]]

if N ==1:
    print(f'{max(game[0])} {min(game[0])}')

for i in range(1,N):
    now = i%2
    before = abs(now-1)

    dp_max[now][0] = game[i][0] + max(dp_max[before][0], dp_max[before][1])
    dp_max[now][1] = game[i][1] + max(dp_max[before][0], dp_max[before][1],dp_max[before][2])
    dp_max[now][2] = game[i][2] + max(dp_max[before][1], dp_max[before][2])

    dp_min[now][0] = game[i][0] + min(dp_min[before][0], dp_min[before][1])
    dp_min[now][1] = game[i][1] + min(dp_min[before][0], dp_min[before][1], dp_min[before][2])
    dp_min[now][2] = game[i][2] + min(dp_min[before][1], dp_min[before][2])

    if i == N-1:
        print(f'{max(dp_max[now])} {min(dp_min[now])}')

# max_game = game[0]
# min_game = game[0]

# # 최대
# max_game = [item[:] for item in game]
# # 최소

#
# for i in range(1,N):
#     max_game[i][0] += max(max_game[i-1][0], max_game[i-1][1])
#     max_game[i][1] += max(max_game[i - 1][0], max_game[i - 1][1], max_game[i - 1][2])
#     max_game[i][2] += max(max_game[i-1][1], max_game[i-1][2])
#
#     min_game[i][0] += min(min_game[i-1][0], min_game[i-1][1])
#     min_game[i][1] += min(min_game[i - 1][0], min_game[i - 1][1], min_game[i - 1][2])
#     min_game[i][2] += min(min_game[i-1][1], min_game[i-1][2])

# print(min(min_game[N-1]))