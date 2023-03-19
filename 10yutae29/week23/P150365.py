# P150365_미로 탈출 명령어

def solution(n, m, x, y, r, c, k):


    # 하 좌 우 상
    dy = [0, -1, 1, 0]
    dx = [1, 0, 0, -1]
    di = ['d', 'l', 'r', 'u']
    stack = [[x, y, 0]]

    now = 0
    word = []
    answer = 'zzzzz'
    while stack:
        x, y, d_start = stack.pop()

        if now == k:
            if y == c and x == r :
                answer = ''.join(word)
                break
            word.pop()
            now -= 1
            continue

        for d in range(d_start, 4):
            next_y = y + dy[d]
            next_x = x + dx[d]
            if 0 < next_x <= n and 0 < next_y <= m :
                stack.append([x, y, d+1])
                now += 1
                word.append(di[d])
                # if now == k:
                #     if next_x==r and next_y == c and
                stack.append([next_x, next_y, 0])
                break
        else:
            if word:
                word.pop()
            now -= 1

    if answer == 'zzzzz':
        answer = 'impossible'
    return answer

print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
print(solution(3,3,1,2,3,3,4))