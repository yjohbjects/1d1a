# Bakjoon 25305 - 커트라인

# input
N, M = map(int, input().split())
score_list = list(map(int, input().split()))

# 정렬
for i in range(N):
    max_idx = i
    for j in range(i + 1, N):
        if score_list[max_idx] < score_list[j]:
            score_list[j], score_list[max_idx] = score_list[max_idx], score_list[j]

print(score_list[M-1])