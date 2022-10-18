# 첫째 줄 조카의 수 M, 과자의 수 N
M, N = map(int,input().split())
snack = list(map(int,input().split()))
# 이진 탐색으로 풀자
start, end = 1, max(snack)
result = 0
while start <= end :
    mid = (start+end)//2
    if sum([n//mid for n in snack]) >= M :
        result = mid
        start = mid+1
    else :
        end = mid-1

print(result)