# B10825_국영수

num = int(input())

students = []
for i in range(num):
    infos = input().split()
    for in_idx in range(len(infos)):
        if infos[in_idx].isnumeric():
            infos[in_idx] = int(infos[in_idx])
    students.append(infos)

answer = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for k in range(num):
    print(answer[k][0])
