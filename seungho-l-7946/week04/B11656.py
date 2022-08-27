# Bakjoon 11656 - 접미사 배열

text = input()
text_list = []

for i in range(len(text)):
    text_list.append(text[i:])

text_list = sorted(text_list)

print(*text_list, sep='\n')