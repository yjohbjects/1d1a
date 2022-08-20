import sys
sys.stdin = open('input_S5097.txt')

T = int(input())
cnt = 1

while T > 0:
    # 리스트의 크기와 회전을 해줄 횟수
    N, M = map(int, input().split())
    # 문제에서 주어진 리스트
    num_lst = list(map(int, input().split()))
    # 총 M회 반복
    for i in range(M):
        element = num_lst.pop(0)  # 리스트의 맨 앞 숫자를 빼내어
        num_lst.append(element)  # 리스트의 맨 뒤로 추가
    print(f'#{cnt} {num_lst[0]}')  # 리스트의 현재 맨 앞에 있는 수 출력
    T -= 1
    cnt += 1