import sys
sys.stdin = open('input_S7701.txt')

T = int(input())
cnt = 1

while T > 0:
    # 명부의 이름 수를 변수로 받음
    N = int(input())
    # 중복되는 이름을 빼주기 위해서 세트로 변수를 받아줌
    name_lst = set(input() for _ in range(N))
    # 정렬을 위해 다시 리스트로 복원
    name_lst = list(name_lst)
    # 우선 이름을 순서에 맞게 정렬해주고
    name_lst = sorted(name_lst)
    # 문제에서 요구한 이름 길이 오름차순으로 정렬해준다
    name_lst = sorted(name_lst, key=len)
    print(f'#{cnt}')
    for name in name_lst:
        print(name)
    T -= 1
    cnt += 1