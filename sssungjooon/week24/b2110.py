import sys

# 백준 2110번 공유기 설치
# 도현이의 집 N개가 수직선 위에 있다.
# 각각의 집의 좌표는 x1, ..., xN
# 집 여러개가 같은 좌표를 가지는 일은 없다.
# 한 집에는 공유기를 하나까지만 설치 가능 (공유기의 개수 C (2 ≤ C ≤ N))
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성

# 이분 탐색으로 풀어보자
# start, end, mid는 공유기 사이의 거리
def binary_search(start, end) :
    answer = 0
    while start <= end :
        mid = (start + end) // 2
        # 항상 첫 집부터 시작
        current = house[0]
        # 공유기를 설치한 횟수 count
        count = 1
        # 공유기 간의 거리를 기반으로 이분탐색 진행할 때, 공유기가 몇 개 설치되는지 for문 진행
        # 좌표가 아닌 집과 집 간의 공유기 거리를 기반으로 이분탐색 진행
        for i in range(1, len(house)) :
            # 현재 집에서 공유기 사이 거리값 중간값을 더한것보다 짧다면  
            if house[i] >= current + mid :
                current = house[i]
                count += 1
        # 공유기를 설치한 횟수가 주어진 공유기 개수 C 이상이면
        if count >= C :
            # 공유기 사이 거리 넓히고,
            start = mid + 1
            # 공유기 사이 최대 거리를 나타내는 answer 값을 mid로 갱신
            answer = mid
        else :
            # C 미만이면 사이 거리 좁히기
            end = mid - 1
    return answer

input = sys.stdin.readline
# 집 개수 N, 공유기 C개 설치
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
# 받은 좌표 정렬
house.sort()

# start 는 최소거리 (좌표가 겹치지 않으므로)
start = 1
# end는 최대 거리
end = house[-1] - house[0]
result = binary_search(start, end)
print(result)
