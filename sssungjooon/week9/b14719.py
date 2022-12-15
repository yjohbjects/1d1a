# 2차원 세계의 세로 길이 H, 2차원 세계의 가로 길이 W
H, W = map(int,input().split())

# 블록 높이 인풋
block = list(map(int,input().split()))

rain = 0
# 빗물이 고이기 위해서는 양쪽이 자신의 지역보다 더 높게 막혀있어야 한다.
# 어차피 양 맨 끝은 빗물이 차도 막는게 없어서 빠지기 때문에 범위에서 뺀다.
for i in range(1, W - 1):
    # 자신을 기준으로 왼쪽 중에 최고치
    left_max = max(block[:i])
    # 자신을 기준으로 오른쪽 중 최고치
    right_max = max(block[i+1:])

    # 그 양쪽 최고치 중 더 낮은 값을 빗물이 받아질 수 있는 최대 높이로
    rain_height = min(left_max, right_max)

    # 빗물이 받아질 수 있는 높이보다 현재 땅의 높이가 낮을 때만 빗물의 양을 측정
    if block[i] < rain_height :
        rain += rain_height - block[i]

print(rain)