import sys
sys.stdin = open('input_B10825.txt')

N = int(input())
# 학생들의 이름과 국영수 점수를 전부 문자열로 받아줌
name_score = [list(map(str, input().split())) for _ in range(N)]
# 점수는 정수로 바꿔주는 작업을 진행
for lst in name_score:
    lst[1] = int(lst[1])
    lst[2] = int(lst[2])
    lst[3] = int(lst[3])
# 리스트를 정렬해주는데 국어 영어 수학 이름 순으로 정렬을 한번에 쓰윽 돌림
name_score = sorted(name_score, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(name_score[i][0])
