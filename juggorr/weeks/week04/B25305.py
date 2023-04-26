def b_sort(N):
    for i in range(len(N), 1, -1):
        for j in range(0, i - 1):
            if N[j] > N[j + 1]:
                N[j], N[j + 1] = N[j + 1], N[j]

N, k = map(int, input().split())
scores = list(map(int, input().split()))
b_sort(scores)

print(scores[N - k])