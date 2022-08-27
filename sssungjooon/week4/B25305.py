import sys
sys.stdin = open("25305.txt")

# 2022 연세대학교 미래캠퍼스 슬기로운 코딩생활에 N명의 학생들이 응시했다.
# 이들 중 점수가 가장 높은 k명은 상을 받을 것이다. 
# 이 때, 상을 받는 커트라인이 몇 점인지 구하라.
# 커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다.

# 첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어진다.
N, k = map(int,input().split())
score = list(map(int,input().split()))

# 버블 정렬로 순서 구현
for i in range(len(score) - 1, 0, -1):
        for j in range(0, i):
            if score[j] < score[j + 1]:
                score[j], score[j + 1] = score[j + 1], score[j]

# 인덱싱으로 프린트
print(score[k-1])