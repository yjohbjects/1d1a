# B2565_전깃줄

n = int(input())

lines = []
for _ in range(n):
    lines.append(list(map(int,input().split())))

lines.sort()
# print(lines)
ans = 0

# 기울기가 - + 면 가장 아래 제거
# 기울기가 + - 면 중간 제가

# slope가 true면 기울기가 +
# false면 기울기가 -
for i in range(1,n-1):
    slope_1 = (lines[i][1] - lines[i-1][1]) > 0
    slope_2 = (lines[i+1][1] - lines[i][1]) > 0
    if slope_1 == False and slope_2 == True:
        ans+= 1
    if slope_1 == True and slope_2 == False:
        ans+= 1
        lines[i] = lines[i-1]
print(ans)