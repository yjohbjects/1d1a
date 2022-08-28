name = input()
names = []

temp = ''
for i in range(len(name)-1, -1, -1):
    temp = name[i] + temp
    names.append(temp)

names = sorted(names, key=lambda x:x)

# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# for x in range(len(name)-1, 0, -1):
#     for y in range(0, x):
#         if alphabets.find(names[y][0]) > alphabets.find(names[y+1][0]):
#             names[y], names[y+1] = names[y+1], names[y]
#         elif alphabets.find(names[y][0]) == alphabets.find(names[y+1][0]):
#             x = 1
#             while x < len(names[y]):
#                 if alphabets.find(names[y][x]) == alphabets.find(names[y+1][x]):
#                     x += 1
#                     continue
#                 else:
#                     if alphabets.find(names[y][x]) > alphabets.find(names[y+1][x]):
#                         names[y], names[y+1] = names[y+1], names[y]
#                     break

for name in names:
    print(name)
