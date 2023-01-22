# P81303_표 편집


def solution(n, k, cmd):
    answer = ''
    ox = ['O'] * n
    rows = list(range(n))

    now = k
    d_stack = []
    for command in cmd:

        if command[0] == 'C':
            num = rows.pop(now)
            d_stack.append([num,now])
            if now == len(rows):
                now -= 1
        elif command[0] == 'Z':
            num, spot = d_stack.pop()
            rows.insert(spot,num)
            if spot <= now:
                now += 1
        else:
            command = command.split()
            do, distance = command
            if do == 'D':
                now += int(distance)
            elif do == 'U':
                now -= int(distance)

    for li in d_stack:
        ox[li[0]] = 'X'

    answer = ''.join(ox)
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))