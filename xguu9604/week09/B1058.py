N = int(input())
friends = [list(map(str, input())) for _ in range(N)]
friends_2 = [[] for _ in range(N)]
answer = [[] for _ in range(N)]
# 1번 친구 찾기
for i in range(N):
    for j in range(N):
        if friends[i][j] == 'Y':
            friends_2[i].append(j)

# 해당 번호의 1번 친구를 바탕으로 2번 친구 찾기
for idx, lst in enumerate(friends_2):
    for friend in lst:
        for j in range(N):
            if friends[friend][j] == 'Y' and j != idx:
                answer[idx].append(j)

inssa = 0
# 중복을 빼면서 2친구 찾아서 최대값 구하기
for i in range(N):
    num = len(set(friends_2[i] + answer[i]))
    if num > inssa:
        inssa = num
print(inssa)
