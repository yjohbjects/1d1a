import sys
sys.stdin = open('7701.txt')

# 길이 순으로 버블소트하는 함수
def b_sort_len(N):
    for i in range(len(N), 1, -1):
        for j in range(0, i - 1):
            if len(N[j]) > len(N[j + 1]):
                N[j], N[j + 1] = N[j + 1], N[j]

# 알파벳 순으로 버블소트하는 함수
def b_sort_len(N):
    for i in range(len(N), 1, -1):
        for j in range(0, i - 1):
            if len(N[j]) > len(N[j + 1]):
                N[j], N[j + 1] = N[j + 1], N[j]

T = int(input())
for tc in range(T):
    N = int(input())
    names = []
# 이름 입력 받기
    for _ in range(N):
        names.append(input())
# 중복 값 제거
    nameset = set(names)
    name_lst = list(nameset)
# 길이 순으로 정렬하기
    b_sort_len(name_lst)
    print(name_lst)

# 알파벳 순으로 정렬하기
