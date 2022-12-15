# B14244 트리 만들기
# https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

# 시작 노드
cnt = 0
print(0, 1)

# 인싸 노드
cnt = 2
node = 1
while cnt <= m:
    print(node, cnt)
    cnt += 1

while cnt < n:
    print(cnt - 1, cnt)
    cnt += 1

