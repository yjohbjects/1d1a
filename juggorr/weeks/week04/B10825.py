T = int(input())
stu_sco = []
for _ in range(T):
    a, b, c, d = list(input().split())
    stu_sco.append([a, int(b), int(c), int(d)])

stu_sco.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in stu_sco:
    print(i[0])