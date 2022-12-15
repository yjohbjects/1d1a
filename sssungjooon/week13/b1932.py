# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 
# 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
n = int(input())

# 0으로 채워진 배열 만들고
arr = []
for _ in range(n):
    temp = [0]*n
    arr.append(temp)

# 인풋값을 넣어준다.
for i in range(n) :
    temp = list(map(int,input().split()))
    for t in range(len(temp)):
        arr[i][t] = temp[t]

# 
# 삼각형의 두번째 열부터 시작
for i in range(1, n):
    for j in range(i+1) :
        # 파스칼의 삼각형 때처럼 더해준다.
        # 맨 왼쪽의 값의 경우 왼쪽 밖에 선택지가 없으므로
        # 한칸 밑의 값을 더해준다. 
        if j == 0 :
            arr[i][j] += arr[i-1][j]

        # 삼각형 젤 오른쪽일 경우 오른쪽 밖에 선택지가 없다.
        elif j == i :
            arr[i][j] += arr[i-1][j-1]
        
        # 그 밖의 케이스의 경우에 왼쪽, 오른쪽 값 중 더 큰 값을 넣어줘야 최대가 된다.
        else :
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

    # 위의 값들을 아래에 더하는 식이므로
    # 제일 끝 값의 최대값이 최대가 되는 경로가 된다.

print(max(arr[n-1]))