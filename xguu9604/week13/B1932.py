'''
재귀함수를 이용해서 풀어보려고 했는데 prunning이 안되는 문제라서 사용불가
그래서 DP를 이용한 풀이를 만들어봤어요
'''


N = int(input())
# 문제에서 주어진 숫자들을 삼각형으로 받아주기
triangle = [list(map(int, input().split())) for _ in range(N)]
# 삼각형과 똑같이 생긴 삼각형을 만들고 이 안에 각 원소의 최대 합을 담아준다
sums = [[0] * i for i in range(1, N+1)]
# 한줄씩 내려가면서 값을 구하자
for i in range(N):
    # 맨 위 꼭대기는 값을 그냥 넣어주자
    if not i:
        sums[i][0] = triangle[0][0]
    # 그 아래부터는 반복 시작
    else:
        # 가로로 한칸씩 순회하는 반복
        for j in range(i+1):
            # 맨 왼쪽 원소의 경우 합구하기
            if not j:
                sums[i][j] = sums[i-1][j] + triangle[i][j]
            # 맨 오른쪽 원소의 경우 합구하기
            elif j == i:
                sums[i][j] = sums[i-1][j-1] + triangle[i][j]
            # 그 외의 친구들은 위에 있는 합중에 최댓값을 뽑아서 계산
            else:
                sums[i][j] = triangle[i][j] + max(sums[i-1][j], sums[i-1][j-1])
# 답은 맨밑줄의 값들 중 최댓값
print(max(sums[-1]))