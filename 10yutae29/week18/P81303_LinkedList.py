# P81303_표 편집_Linked List 도전

def find_val(lili:list, now:int):
    ans = now
    while lili[ans][0] != lili[ans][1]:
        ans += 1
    return ans

def find_start(lili:list, end:int):
    ans = end
    while lili[ans][1] != lili[ans][0]:
        ans -= 1
    return ans

def solution(n, k, cmd):
    linked_list = []
    for i in range(n):
        linked_list.append([i, i])
    # [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]

    now = k
    head = 0
    tail = n-1
    d_stack = []
    for command in cmd:
        if command[0] == "U":
            now -= int(command[2])
        elif command[0] == "D":
            now += int(command[2])
        elif command[0] == "C":
            node = 0
            for i in range(now):
                node = find_val(linked_list,node) + 1
            # 노드의 끝 value값을 찾아서 삭제해줌
            linked_list[node][1] += 1
            d_stack.append(node)
            if linked_list[node][1] > tail or find_val(linked_list, now) > tail:
                now -= 1
                tail -= 1

        else:
            restore = d_stack.pop()
            linked_list[restore][1] = restore
            if restore < find_val(linked_list,now):
                now += 1
            if restore > tail:
                tail = restore
    ox = ['O'] * n
    for x in d_stack:
        ox[x] = 'X'
    answer = ''.join(ox)

    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

