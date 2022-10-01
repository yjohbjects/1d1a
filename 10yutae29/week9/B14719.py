# B14719 빗물

H, W = map(int, input().split())

blocks = list(map(int, input().split()))


real_block = [[0]*W for _ in range(H)]
for w in range(W):
    block = blocks[w]
    for h in range(H-1, H-block-1, -1):
        real_block[h][w] = 1

rain = 0

for floor in real_block:
    state = 0
    between = 0

    for one_block in floor:

        if state == 1 and one_block == 1:
            rain += between
            between = 0

        elif one_block == 1:
            state = 1

        if state==1 and one_block == 0:
            between += 1
print(rain)

