# BAEKJOON 3085 - 사탕 게임 (S2)

'''
문제
1) N×N크기에 사탕을 채워 놓는다.
2) 사탕의 색이 다른 인접한 두 칸을 고르고, 고른 칸에 들어있는 사탕을 서로 교환
3) 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹음
4) 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램

풀이
1) 행과 열별로 먹을 수 있는 최대한의 캔디 수를 세는 함수를 정의
2) matrix와 transposed matrix로 나누어가 각각 다른 문자를 바꿔주는 반복문 작성
3) 해당 반복문 내에서 1번의 함수를 반복하여 돌려서
4) 최대값을 도출

입력
1) 첫째 줄에 보드의 크기 N
2) 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다.
3) 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
4) 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어짐

출력
1) 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력
'''

import sys

sys.stdin = open('B3085.txt')

# 캔디 얼마나 먹는지 반환하는 함수
def eat_candy(matrix, N):

    # 최대 캔디 변수 선언
    max_candy = 0

    # matrix
    for i in range(N):

        # 각종 변수 선언
        # 최종 캔디 수, 캔디 수 세는 변수, 비교 문자(같은지)
        max_candy_count = 0
        candy_count = 0
        comparison_candy = ''

        # 열별로 비교
        for candy in matrix[i]:

            # 비교 문자 비어있을 경우 채워주고 카운트 + 1
            if not comparison_candy:
                comparison_candy = candy
                candy_count += 1

            # 문자 안비어있을 경우
            else:

                # 비교군과 실험군이 같은 경우
                if comparison_candy == candy:

                    # 카운트 + 1
                    candy_count += 1

                # 아닌 경우
                else:

                    # 비교 문자 바꿔주고
                    comparison_candy = candy

                    # 카운트 수 초기화
                    candy_count = 1

                # 카운트 수가 최종 캔디 수보다 크면 갱신
                if candy_count > max_candy_count:
                    max_candy_count = candy_count

        # 열별 비교군에서 가장 큰 카운트 값이 최종 return 값보다 클 경우 갱신
        if max_candy < max_candy_count:
            max_candy = max_candy_count

    # transpose matrix로 같은 과정 반복
    matrix_T = list(map(list, zip(*matrix)))

    for j in range(N):

        max_candy_T_count = 0
        candy_T_count = 0
        comparison_candy_T = ''
        for candy in matrix_T[j]:
            if not comparison_candy_T:
                comparison_candy_T = candy
                candy_T_count += 1
            else:
                if comparison_candy_T == candy:
                    candy_T_count += 1
                else:
                    comparison_candy_T = candy
                    candy_T_count = 1
                if candy_T_count > max_candy_T_count:
                    max_candy_T_count = candy_T_count

        if max_candy < max_candy_T_count:
            max_candy = max_candy_T_count

    return max_candy

# input
N = int(input())
candy_mat = [list(input()) for _ in range(N)]

# matrix transpose
candy_mat_T = list(map(list, zip(*candy_mat)))

# result list
result = []

# matrix
for i in range(N):
    for j in range(N - 1): # 앞뒤를 바꿀것이기 때문에 j index는 N - 1
        
        # 이전 요소와 다를 경우
        if candy_mat[i][j] != candy_mat[i][j + 1]:
            
            # 바꿔주기
            candy_mat[i][j], candy_mat[i][j + 1] = candy_mat[i][j + 1], candy_mat[i][j]
            
            # 함수 결과 값 result에 추가
            result.append(eat_candy(candy_mat, N))
            
            # 자기 원위치
            candy_mat[i][j], candy_mat[i][j + 1] = candy_mat[i][j + 1], candy_mat[i][j]

# transpose matrix로 같은 과정 반복
for i in range(N):
    for j in range(N - 1):
        if candy_mat_T[i][j] != candy_mat_T[i][j + 1]:
            candy_mat_T[i][j], candy_mat_T[i][j + 1] = candy_mat_T[i][j + 1], candy_mat_T[i][j]
            result.append(eat_candy(candy_mat_T, N))
            candy_mat_T[i][j], candy_mat_T[i][j + 1] = candy_mat_T[i][j + 1], candy_mat_T[i][j]

# output
print(max(result))