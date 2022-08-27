# 미로

'''
NxN 크기의 미로에서 출발에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
2에서 출발해서 3으로 도착할 수 있는지 확인하면 된다.

1. 탐색함수 설계
> 미로 밖으로 갈수없음
> 목적지 도착 True 반환
> 벽에는 갈 수 없음
> 지나온 길은 체크
> 4방향으로 재귀함수

2. 초기 좌표 설정
3. 정방향으로 시도 후, 안될 경우 반대방향 시도
4. 가능, 불가능 판단
'''

import sys
sys.stdin = open("S4875.txt")

# 1. 탐색함수 설계
def search(x,y,d):

    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if mat[x][y] == 3:
        return True

    elif mat[x][y] == 1:
        return False        

    elif mat[x][y] == 0 or mat[x][y] == 2:
        mat[x][y] = 1

        if d == 1:
            return search(x-1, y, 1) or search(x, y-1, 1) or search(x+1, y, 1) or search(x, y+1, 1)

        elif d == -1:
            return search(x, y+1, -1) or search(x+1, y, -1) or search(x, y-1, -1) or search(x-1, y, -1)

num = int(input())

for tc in range(1, num+1):

    # iuput
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]

    # 2. 초기 좌표 설정
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                x, y = i, j
    
    # 초기 좌표 고정
    fix_x, fix_y = x, y

    while True:
        
        if search(x, y, 1) == True: # 정방향으로 시도
            result = True
            break
        else:
            x, y = fix_x, fix_y # 좌표 초기화
            if search(x, y, -1) == True: # 반대방향으로 시도
                result = True
                break
            else:
                result = False
                break
        
    print(f'#{tc} {int(result)}')