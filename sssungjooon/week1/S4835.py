# 첫 줄에 테스트 케이스 개수 T
# 둘째 줄 정수의 개수 N과 구간의 개수(구간 안에 있는 정수의 개수) M 
# 셋째 줄 N개의 정수들

T = int(input())
# 10 <= N <= 100
# 2 <= M < N


# 테스트 횟수 T만큼 N, M을 넣어야 하므로 반복문 사용
# 그 다음의 N개의 정수들을 리스트에 넣어야 하므로 Num_list에 넣기
for test_num in range(1,T+1):
    N, M = map(int,input().split())
    Num_list = list(map(int,input().split()))
    # 구간합을 넣을 리스트 만들기
    Sum_list = []
    # N-M+1 = 구간을 정할 수 있는 범위, 구간 시작점
    for i in range(N-M+1):
        result = 0
        for num in range(i,i+M):
        # 구간 시작점인 i부터 구간 개수만큼 더해서 result에 넣기
        # num은 해당 구간에 있는 정수들
            result += Num_list[num]
        # 각 구간들의 합인 result 값을 Sum_list에 넣자
        Sum_list.append(result)
    # 이 구간 합을 넣은 Sum_list의 최대값과 최소값을 빼면 구할 수 있다.
    # 출력을 #t 구간합 : 이런식으로 나타내야 하므로
    print("#%d %d"%(test_num,max(Sum_list)-min(Sum_list)))