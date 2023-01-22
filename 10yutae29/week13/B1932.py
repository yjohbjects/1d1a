# B1932_정수 삼각형

# 맨 아래층부터 올라가면서 수를 더할 때 그 값이 최대가 되도록 dp진행

# 삼각형의 크기
n = int(input())

# 삼각형에 부여된 수
triangle = [list(map(int, input().split())) for _ in range(n)]

# n-1층부터 두갈래의 아래층 숫자중 더큰 수를 더하면서 1층까지 간다
for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])

