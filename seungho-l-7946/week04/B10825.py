# Bakjoon 10825 - 국영수

N = int(input())
score_list = [input().split() for _ in range(N)]
for i in range(len(score_list)):
    for j in range(len(score_list[i])):
        if score_list[i][j].isnumeric():
            score_list[i][j] = int(score_list[i][j])
score_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(len(score_list)):
    print(score_list[i][0])
