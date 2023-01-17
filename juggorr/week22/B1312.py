import sys
sys.stdin = open('in.txt')
A, B, N = map(int, sys.stdin.readline().split())


# B가 몇 자리 수인지 세기 위해서
b = len(str(B))

# 정수까지 다 다누고 시작하고 시픔
r = A % B
A = r
# 소수점밑에 자리수가 추가될때마다 cnt + 1
# cnt = N 이 되면 반복문 종료
cnt = 0

while True:
    # 나머지 구하기
    R = A % B

    sR = str(R)
    sR += '0'
    A = int(sR)

    Q = A // B
    cnt += 1

    if cnt == N:
        print(Q)
        break