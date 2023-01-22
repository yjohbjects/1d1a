# B6236_용돈 관리

N, M = map(int,input().split())

# 매일 써야하는 돈 리스트
days = []
for n in range(N):
    days.append(int(input()))

# 이진탐색 시작점
# 최소값은 써야하는 돈의 하루 최대값
start = max(days)
# 최대값은 써야하는 돈을 합한 값
end = sum(days)

# 이진탐색
while True:
    # 중간값 설정 / 중간값을 K로 설정
    mid = (start + end) // 2

    # 통장에서 돈을 뺴는 횟수(일단 한번 뺸걸로 시작해서 1)
    m_count = 1
    # days 리스트를 순회할 인덱스 0 ~ len(days)-1
    d_count = 0
    # 처음에 K만큼 돈을 뽑았으니 수중에 남은 돈 = K
    m_rest = mid

    # 매일 돈을 소비
    while d_count<len(days) and m_count <= M:

        # 수중에 남은 돈이 그날 써야할 돈보다 많다면
        if m_rest >= days[d_count]:
            # 수중에 남은돈 - 그날 써야할 돈
            m_rest -= days[d_count]
            # 다음날로 이동
            d_count += 1

        # 수중에 남은 돈이 그날 써야할 돈보다 부족하다면
        else:
            # 통장에 남은 돈을 넣고 다시 K만큼 인출
            m_rest = mid
            # 인출 횟수 + 1
            m_count += 1


    # 만약 인출횟수가 M보다 많다면
    if m_count > M:
        # 현재의 K값(mid)으로는 부족하니 더 높은 범위 탐색
        start = mid + 1

    # 만약 모든날의 돈을 M보다 적은 수로 인출하여 소비 가능하다면
    elif d_count==len(days):
        # 현재 K값(mid)으로는 충분하니 더 낮은 범위 탐색
        end = mid - 1
        # K값을 mid로 업데이트    K  <- 현재 K값(mid)
        K = mid

    # 탐색범위의 시작점과 끝점이 같아지면
    if start == end:
        # 그때 K = start = end 로 최소의 K값이 된다.
        K = start
        break

print(K)


