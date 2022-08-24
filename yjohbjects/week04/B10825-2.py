from pprint import pprint

# B10824 국영수
N = int(input())


scores = list(list(map(str, input().split())) for _ in range(N))
for z in range(N):
    scores[z][1], scores[z][2], scores[z][3] = int(scores[z][1]), int(scores[z][2]), int(scores[z][3])

scores.sort(key=lambda x:x[0])
scores.sort(key=lambda x:x[3], reverse=True)
scores.sort(key=lambda x:x[2])
scores.sort(key=lambda x:x[1], reverse=True)


for q in range(N):
    print(scores[q][0])