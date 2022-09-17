# DFS 함수 정의
def DFS(virus) :
    global worm
    check[virus] = 1

    for k in computer[virus] :
        if check[k] == 0 :
            DFS(k)
            worm += 1


# 컴퓨터의 수 C
C = int(input())

# 네트워크 상 연결된 컴퓨터 쌍의 수
T = int(input())

# 0이 아닌 빈칸을 할당 (visited처럼 0을 1로 바꾸는 게 아닌, 각 연결 숫자를 넣어 각 인덱스별 연결 상태를 알 수 있도록 숫자를 삽입하기 때문)
computer = [[]*(C+1) for _ in range(C+1)]

# 웜 바이러스
worm = 0

check = [0] * (C+1)

# 한 줄씩 연결된 컴퓨터 번호의 쌍
for _ in range(T):
    a, b = map(int, input().split())
    # 인덱스 a에 b를 넣고, 인덱스 b에 a를 넣어서 연결됨을 표시한다.
    computer[a].append(b)
    computer[b].append(a)

# print(computer)
DFS(1)

print(worm)
