# BAEKJOON 14719 - 빗물 (G5)

'''
문제
1) 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
2) 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

풀이
1) while과 for문을 활용해 포인터로 문제를 풀어보고자 했으나 실패
2) 이전에 빌딩 조망 문제 용현이가 풀었던 것처럼 열별로 벽의 유무를 파악함
3) 2차 배열로 도식화하여 벽과 벽을 탐색 후, 해당 범위 내 0의 개수를 셈

입력
1) 첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W
2) 두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개
3) 따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정

출력
1) 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력
2) 빗물이 전혀 고이지 않을 경우 0을 출력
'''

import sys

sys.stdin = open('B14719.txt')

# input
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 2차 배열로 받기
block_mat = [[0] * W for _ in range(H)]
result = 0

# blocks의 개수에 맞게 도식화
for idx in range(len(blocks)):
    for x in range(H):
        if x < blocks[idx]:
            block_mat[x][idx] = 1

# 1과 1사이의 0 개수 찾기
for x in range(H):

    # 왼벽, 오른벽 좌표
    left_idx = right_idx = -1

    # 최우선 왼벽 찾기
    for y in range(W):
        if block_mat[x][y] == 1:
            left_idx = y
            break

    # 최우선 오른벽 찾기
    for y in range(W - 1, -1, -1):
        if block_mat[x][y] == 1:
            right_idx = y
            break

    # 둘다 0 이상일 경우만 값이 입력된 것이므로, 해당 케이스일 경우에만 실행
    if left_idx >= 0 and right_idx >= 0:

        # 해당 범위 내 0 개수 찾기
        for idx in range(left_idx + 1, right_idx):
            if block_mat[x][idx] == 0:
                result += 1

# output
print(result)


'''
# 실패한 while 포인터

while left_idx < W and right_idx < W:
    if blocks[left_idx] >= left_wall:
        if right_idx == -1:
            left_wall = blocks[left_idx]
            left_idx += 1
    else:
        for h in range(left_wall):
            for next in range(left_idx, W):
                if blocks[next] >= left_wall - h:
                    right_idx = next
                    break
            if right_idx != -1:
                break

    if left_idx != -1 and right_idx != -1:
        wall_height = min(left_wall, blocks[right_idx])
        for x in range(left_idx, right_idx):
            rain += wall_height - blocks[x]
        left_idx = right_idx
        right_idx = -1
        
        
# 실패한 for 포인터

for idx in range(W):

    if left_idx == -1:
        left_idx = idx

    if right_idx == -1:
        if blocks[idx] >= blocks[left_idx]:
            left_idx = idx
        else:
            for h in range(blocks[left_idx]):
                for next in range(left_idx + 1, W):
                    if blocks[next] >= blocks[left_idx] - h:
                        right_idx = next
                        break
                if right_idx != -1:
                    break

    if left_idx != -1 and right_idx != -1:
        wall_height = min(blocks[left_idx], blocks[right_idx])
        for x in range(left_idx + 1, right_idx):
            rain += wall_height - blocks[x]
            
'''