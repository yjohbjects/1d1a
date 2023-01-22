# B16401_과자 나눠주기

# M: 조카 수, N: 과자 수
M, N = map(int,input().split())

# 과자 N개의 길이가 오름차순으로 정렬된 리스트
snacks = sorted(list(map(int,input().split())))

# 이진탐색 시작점 = 1
start = 1
# 이진탐색 끝점: 가장 긴 과자의 길이
end = snacks[-1]
# ans = 0으로 초기화 / 만약 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없으면 그대로 0이 출력됨
ans = 0

# 이진탐색 시작
while start <= end:
    # 중간점: 조카에게 나눠줄 과자의 길이
    mid = (start + end) // 2

    # mid 길이로 조카에게 줄 수 있는 과자 갯수를 셈
    s_num = 0
    for snack in snacks:
        s_num += snack//mid

    # 조카에게 줄 수 있는 과자 갯수가 M보다 크거나 같으면
    if s_num >= M:
        # 과자를 더 길게 줄 수 있는지 탐색하기위해 start 지점 업데이트
        start = mid + 1
        # ans에 이때 과자길이 일단 입력
        ans = mid
    # 조카에게 줄 수 있는 과자의 갯수가 M보다 작으면
    else:
        # 더 작은 길이로 줄 수 있는지 탐색하기 위해 end 지점 업데이트
        end = mid - 1

# 이진탐색이 종료되면 그때 ans값(조카 1명에게 줄 수 있는 막대과자의 최대길이)을 출력
print(ans)

