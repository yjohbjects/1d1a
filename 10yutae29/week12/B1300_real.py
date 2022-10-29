# B1300_K번째 수

# 배열의 크기
N = int(input())
# 찾아야할 B원소의 인덱스
k = int(input())

x, y = N, N
ans = x*y
cnt = 1
order = N**2 - k

while cnt < order:
    if x == y:
        save = x
        y -= 1
    elif x>y:
        x -= 1
        y = save
    else:
        y -= 1
    ans = x*y
    cnt += 1
print(ans)