def b_sort(N):
    for i in range(len(N), 1, -1):
        for j in range(0, i - 1):
            if N[j] > N[j + 1]:
                N[j], N[j + 1] = N[j + 1], N[j]

lst = [78, 23, 5, 1, 3]

b_sort(lst)

print(lst)