# B11656_접미사 배열

string = input()

st_list = []
for st_idx in range(len(string)):
    st_list.append(string[st_idx::])

# answer = sorted(st_list)
# for ans in answer:
#     print(ans)

for i in range(len(st_list), 0, -1):
    for j in range(1, i):
        if st_list[j] < st_list[j-1]:
            st_list[j], st_list[j-1] = st_list[j-1], st_list[j]
for ans in st_list:
    print(ans)