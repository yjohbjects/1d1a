import sys
sys.stdin = open('input.txt')

'''
백준에서 제시한 그림과 똑같이 생긴 2차원 배열을 만들자
그렇게 되면 생각보다 쉽게 풀린다..
위에서 한 행씩 비가 고일수 있는지 없는지 판단해가면 깔끔
'''

# 최대 높이와 지형의 너비
H, W = map(int, input().split())
# 각 지형의 높이 값을 리스트로 받아줌
heights = list(map(int, input().split()))
# 2차원 배열로 그림을 그려줄 예정
heights_arr = [[0] * W for _ in range(H)]
# 고이는 비
rain = 0
# 2차원 배열의 밑의 행부터 위로 올라가면서 그림을 채워준다
for i in range(H-1, -1, -1):
    for j in range(W):
        # 현재 열의 지형에 높이값이 존재한다면
        if heights[j]:
            # 2차원 배열에 1을 채워주고
            heights_arr[i][j] = 1
            # 지금 열의 높이를 1 깎아준다.
            heights[j] -= 1

# 그림 다 그렸으니 순회 시작
for i in range(H):
    # 빗물이 고일 수 있는 가능성이 있는 칸들을 세어줌
    can_water = 0
    # 왼쪽의 벽을 지나쳐왔는지 유무 판별
    is_wall = False
    # 행에서 한칸씩 옆으로 탐색 시작
    for j in range(W):
        # 벽을 지나쳐 왔다면
        if is_wall:
            # 현재 지점이 벽이 아니라면
            if heights_arr[i][j] == 0:
                # 그 자리에 비가 고일 수 있음을 체크
                can_water += 1
            # 벽을 지나쳐 왔는데 벽을 또 만나면
            else:
                # 고인 빗물에 고일 수 있는 칸의 수를 더해준다
                rain += can_water
                # 그리고 고일 수 있는 칸들을 전부 초기화
                # 현재 지금 위치가 다시 벽이 됨
                # 따라서 is_wall을 False로 초기화할 필요 없음
                can_water = 0
        # 아직 벽을 지나치지 않았다면
        else:
            # 벽을 만났을때
            if heights_arr[i][j]:
                # 벽을 만났다고 체크
                is_wall = True
# 답 출력
print(rain)