import sys
sys.stdin = open('S4869.txt')

# 변형 피보나치 수열을 위한 재귀 함수 만들기
def papers(n):

# 1칸이 더해지는 경우 직사각형을 세로로 더하는 경우만 존재
    if n == 1:
        return 1
        
# 2칸이 더해지는 경우 가로 배열을 고려해 2를 곱함
    elif n == 2:
        return 3
    return papers(n - 1) + 2 * papers(n - 2)


T = int(input())
for tc in range(T):
    N = int(input())
    n = N // 10

    print(f'#{tc + 1} {papers(n)}')