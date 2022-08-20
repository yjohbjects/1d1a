import sys
sys.stdin = open('input_S1961.txt')

'''
문제 설명 : NxN 행렬이 주어지고 그 행렬을 90도 180도 270도 회전한 행렬을 구하는 문제
'''

T = int(input())
cnt = 1

# 시계방향으로 90도 회전을 시켜주는 함수를 정의해줌
def turn(N, arr):
    # 회전해서 나오는 새로운 행렬을 나타내줄 빈 행렬
    new_arr = [[0]*N for _ in range(N)]
    # 한 행씩 기존에 주어진 행렬을 순회한다.
    for i in range(N):
        # 한 행을 순회하면서 그 행을 따로 꺼내와서 담을 빈 리스트
        append_lst = []
        # 그 행을 열별로 순회하면서
        for j in range(N):
            # 각 요소들을 빈 리스트에 추가해준다.
            append_lst.append(arr[i][j])
        # 꺼낸 행을 담은 리스트를 거꾸로 순회하면서
        for k in range(N - 1, -1, -1):
            # 빈 행렬에 오른쪽 밑에서부터 위로 리스트의 마지막 요소를 채워넣어준다
            new_arr[k][N - 1 - i] = append_lst[k]
    # 완성된 행렬 반환
    return new_arr

while T > 0:
    # 받은 행렬의 크기값
    N = int(input())
    # 회전시킬 행렬을 받아줌
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 행렬을 시계방향 90도씩 회전을 3번 진행
    arr_90 = turn(N, arr)
    arr_180 = turn(N, arr_90)
    arr_270 = turn(N, arr_180)
    # 문제에서 요구하는 조건에 맞게 출력
    print(f'#{cnt}')
    # 행단위로 전부 반복
    for i in range(N):
        # 90도 회전한 행렬의 해당하는 i번째 행을 하나씩 나열해주고 끝에 띄어쓰기
        for j in range(N-1):
            print(f'{arr_90[i][j]}', end='')
        print(f'{arr_90[i][N-1]}', end=' ')
        # 180도 회전한 행렬의 해당하는 i번째 행을 하나씩 나열해주고 끝에 띄어쓰기
        for j in range(N-1):
            print(f'{arr_180[i][j]}', end='')
        print(f'{arr_180[i][N-1]}', end=' ')
        # 270도 회전한 행렬의 해당하는 i번째 행을 하나씩 나열해주고 끝에 띄어쓰기
        for j in range(N-1):
            print(f'{arr_270[i][j]}', end='')
        print(f'{arr_270[i][N-1]}', end=' ')
        # 한 행을 다 적어주면 줄바꿈
        print()
    T -= 1
    cnt += 1