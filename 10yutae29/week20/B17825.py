# B17825 주사위 윷놀이

dices = list(map(int, input().split()))

answer = 0

straigt = list(range(0,41,2))
print(straigt)
road_10 = [10, 13, 16, 19, 25, 30, 35, 40]
road_20 = [20, 22, 24, 25, 30, 35, 40]
road_30 = [30, 28, 27, 26, 25, 30, 35, 40]

roads = [straigt, road_10, road_20, road_30]

one, two, three, four = [0,0], [0,0], [0,0], [0,0]

