# 끝나고 제출 전 지울 범위#
# 델타이동 없는 버젼
import sys
sys.stdin = open("1028.txt")

# 다이아몬드 광산은 0과 1로 이루어진 R행*C열 크기의 배열이다.
# 다이아몬드는 1로 이루어진 정사각형의 경계선을 45도 회전시킨 모양이다.
# 크기가 1, 2, 3인 다이아몬드 모양은 다음과 같이 생겼다.
# 다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력하는 프로그램을 작성하시오.

# 광산의 다이아몬드 크기가 큰 순으로 찾아내는 함수를 만든다.
def find_dia(arr, R, C):
    # 우선 사이즈3 다이아부터 찾는데, 3이 되려면 R,C 둘다 5 이상이어야 한다.
    if R >= 5 and C >= 5 :
        # 그 후 범위는 다이아의 중심이 위치할 수 있는 r,c 좌표 안이어야 한다.
        # 사이즈3 다이아의 중심은 광산의 상하좌우에서 각각 3번째 칸이 떨어져야 위치가능
        # 사이즈3 다이아 젤 위왼쪽 위치가능 좌표는 (2,2)
        # 사이즈3 다이아 젤 아래오른쪽 위치가능 좌표는 (R-3, C-3)
        for i in range(2,R-2):
            for j in range(2,C-2):
                # 총 8개의 위치에 1이 있어야 다이아 3 충족
                if arr[i-2][j] == 1 and arr[i-1][j-1] == 1 and arr[i-1][j+1] == 1 and arr[i][c-2] == 1 and arr[i][c+2]==1 and arr[i+1][j-1] == 1 and arr[i+1][j+1] == 1 and arr[i+2][j]== 1 :
                    break
                return 3
    # 사이즈2 다이아 찾기
    elif R >= 3 and C >= 3 :
        for i in range(1,R-1):
            for j in range(1,C-1):
                # 총 4개의 위치에 1이 있어야 다이아 2 충족
                if arr[i-1][j] == 1 and arr[i+1][j]==1 and arr[i][j-1]==1 and arr[i][j+1]==1 :
                    break
                return 2
    # 그 밖의 경우에 사이즈1 다이아 찾거나 0 반환
    else :
        for r in range(R):
            for c in range(C):
                if arr[r][c] == 1 :
                    return 1
                else :
                    return 0

# 다이아 찾는 함수 정의 했으면 시작
T = int(input())
for test_count in range(1,T+1):
    R, C = map(int,input().split())
    # R행 C열 크기의 광산
    mine = []
    # R만큼 반복
    for _ in range(R):
        temp = list(input())
        mine.append(temp)
    result = find_dia(mine, R, C)
    print(f'#{test_count} {result}')