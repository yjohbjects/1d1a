from pprint import pprint

# B10824 국영수
N = int(input())
scores = list(list(map(str, input().split())) for _ in range(N))
alphabets = 'AaBbCcDdEeFfGgEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

for i in range(N-1, 0, -1):
    for j in range(0, i):

        # 4. alphabetical order
        if alphabets.find(scores[j][0][0]) > alphabets.find(scores[j+1][0][0]):
            scores[j], scores[j+1] = scores[j+1], scores[j]
        elif alphabets.find(scores[j][0][0]) == alphabets.find(scores[j+1][0][0]):
            x = 1
            while True:
                if alphabets.find(scores[j][0][x]) == alphabets.find(scores[j+1][0][x]):
                    x += 1
                    continue
                else:
                    if alphabets.find(scores[j][0][x]) > alphabets.find(scores[j+1][0][x]):
                        scores[j], scores[j + 1] = scores[j + 1], scores[j]
                    break

        # 3. math score
        if int(scores[j][3]) < int(scores[j+1][3]):
            scores[j], scores[j+1] = scores[j+1], scores[j]

        # 2. eng score
        if int(scores[j][2]) > int(scores[j + 1][2]):
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

        # 1. kor score
        if int(scores[j][1]) < int(scores[j + 1][1]):
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

for z in range(N):
    print(scores[z][0])