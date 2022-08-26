import sys
sys.stdin = open('input_B25305.txt')
'''
버블 소트 주간 유일한 버블 소트 문제..!
'''
# 학생들의 명수와 커트라인 등수
N, cut = map(int, input().split())
# 점수 리스트를 주르륵 받아줌
score_lst = list(map(int, input().split()))
# 버블 소트를 통해서 내림차순으로 점수를 정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if score_lst[j] < score_lst[j+1]:
            score_lst[j], score_lst[j+1] = score_lst[j+1], score_lst[j]
# 커트라인의 점수를 구하는 것이고 인덱스는 0부터 시작이므로 -1을 해줘야 맞는 등수
print(score_lst[cut-1])