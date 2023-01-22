import sys
sys.stdin = open('in.txt')
from pprint import pprint


H, W = map(int, input().split())
blocks = list(map(int, input().split()))

sdw = [[0] * W for _ in range(H)]
# 2차원 세계 그리기 2가 block 표시
i = 0
for c in range(W):
    for r in range(H -1, -1, -1):
        if blocks[i] > 0:
            sdw[r][c] = 1
        blocks[i] -= 1
        if r == 0:
            i += 1

# row마다 블록 등장 = 새 블록이 등장하고 다음 블록이 등장하면
# 그 사이를 물로 채우기
# 등장하지 않으면 물은 그냥 흘러내림
# 2 0 이 나오면 cnt 세기 시작
# 0 2가 등장하면 카운트 result에 더해주고 초기화
# 0 2가 등장하지 않고 row가 끝나면 그냥 초기화
#

result = 0
for r in range(H):
    water = 0
    wall = False
    fill = False
    for c in range(W):
        # 블록 시작 감지
        if sdw[r][c] == 1:
            wall = True
        # 블록이 있는 상태고 빈공간이 등장한다면
        # 채우기 시작
        if wall and sdw[r][c] == 0:
            fill = True

        if wall and fill and sdw[r][c] == 0:
            water += 1

        # 새로운 벽이 등장한다면
        # 물 세고 초기화 하기
        if wall and fill and sdw[r][c] == 1:
            result += water
            water = 0

print(result)