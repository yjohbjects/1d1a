# B12865_평범한 배낭

# N : 물건 수 , K : 배낭이 담을 수 있는 최대 무게
N, K = map(int, input().split())

# 물건의 (무게, 가치)를 담을 리스트
stuff = []
for n in range(N):
    W, V = map(int, input().split())
    stuff.append([W, V])
# 물건의 무게를 기준으로 오름차순으로 정렬
stuff.sort()


# 2차원 dp를 사용하기 위한 2차원 배열
dp_arr = [[0] * (K+1) for _ in range(N+1)]

# i는 현재 배낭에 넣으려는 물건
# 인덱스로는 i-1
for i in range(1,N+1):
    # 현재 배낭에 넣으려는 물건의 무게와 가치
    weight = stuff[i-1][0]
    value = stuff[i-1][1]
    # j는 배낭에 넣을 수 최대 무게
    for j in range(1,K+1):
        if weight <= j:
            # 현재 넣으려는 물건의 무게가 현재 배낭에 넣을 수 있는 최대 무게보다 작다면
            # 배낭에 물건을 넣을지 말지 결정해야함
            #
            dp_arr[i][j] = max(value + dp_arr[i-1][j-weight], dp_arr[i-1][j])
        else:
            dp_arr[i][j] = dp_arr[i-1][j]

print(dp_arr[-1][-1])