# B16401 과자 나눠주기
# https://www.acmicpc.net/problem/16401

'''
나누어줄 수 있는 과자의 개수를 이진탐색한다.
1부터 candy 리스트의 maximum value까지가 경우의 수
'''

M, N = map(int, input().split())
candies = list(map(int, input().split()))

start = 1
end = max(candies)

maxV = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for candy in candies:
        cnt += candy // mid

    # 캔디를 M명의 조카에게 나누어 줄 수 있고 최대 길이라면 값을 저장
    if cnt >= M and mid > maxV:
        maxV = mid
        # 값을 저장하고 다음 탐색을 위해 우측 이진탐색 ㄱ
        start = mid + 1

    # 캔디를 모든 조카에게 나누어 줄 수 없다면, 다음 탐색 좌측 이진탐색 ㄱ
    else:
        end = mid - 1

print(maxV)

