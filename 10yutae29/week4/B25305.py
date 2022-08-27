# B25305 커트라인

num, cut = map(int, input().split())

scores = list(map(int, input().split()))

for i in range(num, 0, -1):
    for j in range(1, i):
        if scores[j-1] < scores[j]:
            scores[j], scores[j-1] = scores[j-1], scores[j]

print(scores[cut-1])
