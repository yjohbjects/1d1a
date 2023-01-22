from pprint import pprint

# B10824 국영수
N = int(input())

scores = list(list(map(str, input().split())) for _ in range(N))
for z in range(N):
    scores[z][1], scores[z][2], scores[z][3] = int(scores[z][1]), int(scores[z][2]), int(scores[z][3])

scores = sorted(scores, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for x in range(N):
    print(scores[x][0])