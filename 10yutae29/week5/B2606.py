# B2606 바이러스

c_num = int(input())
cs_num = int(input())

c_list = [[] for _ in range(c_num+1)]
for _ in range(cs_num):
    a, b = map(int, input().split())
    c_list[a].append(b)
    c_list[b].append(a)

after_len = 100
before_len = 0
one_list = c_list[1][::]
while after_len != before_len:
    before_len = len(one_list)
    for i in one_list:
        for j in c_list[i]:
            if j not in one_list:
                one_list.append(j)
    after_len = len(one_list)

print(len(set(one_list))-1)