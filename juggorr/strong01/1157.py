import sys

# 파이썬 대문자 소문자 .upper() / .lower()
word = sys.stdin.readline().rstrip().upper()

# 캐릭터 숫자 셀 dict
char_dict = {}

# 캐릭터 순회하면서 dict에 넣기
for char in word:
    # 이미 있다면
    if char in char_dict:
        # 갯수 1 더해주기
        char_dict[char] += 1
    # 없다면
    else:
        # 처음으로 세주기
        char_dict[char] = 1

# 각각 dict의 아이템, value, key에 접근하는 방법
print(char_dict.items())
print(char_dict.values())
print(char_dict.keys())



# 갯수 비교할 list
char_cnt_list = []
# 딕셔너리 순회하면서 최댓값 기록하기
for key in char_dict:
    char_cnt_list.append([char_dict[key], key])

char_cnt_list.sort(key=lambda x: -x[0])

if len(char_cnt_list) < 2:
    print(char_cnt_list[0][1])
else:
    if char_cnt_list[0][0] == char_cnt_list[1][0]:
        print('?')
    else:
        print(char_cnt_list[0][1])