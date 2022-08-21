import sys
sys.stdin = open("5097.txt")

# N개의 숫자로 이루어진 수열이 주어진다.
# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때,
# 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

T = int(input())

for test_count in range(1,T+1) :
    N, M = map(int,input().split())
    num_list = list(map(int,input().split()))

    # N과 M 사이의 공식을 파악하기 위해 예시를 들어보자
    # listA = [a, b, c] 일때, N = 3인데, M = 10일 경우
    # 맨 앞의 숫자 맨 뒤로 보내는 작업을 3번 했을 때 원래의 배치가 된다.
    # 따라서 작업을 N번 했을 때마다 원래의 배치가 되고, 작업 횟수 M번을 N으로 나눈 나머지만 찾으면 된다.
    # M%N = 1 이므로, N=3일 때 작업횟수 10번과 1번은 동일하다.

    for i in range(M % N):
        # append와 remove를 이용하면 첫 요소를 오른쪽 맨 끝으로 옮기기 가능
        num_list.append(num_list[0])
        num_list.remove(num_list[0])
    print(f'#{test_count} {num_list[0]}')