# P132265_롤케이크 자르기

def solution(topping):
    answer = 0
    equal = 0

    left = topping[::]
    right = []
    r_set = set()
    for i in range(len(topping)):
        t = left.pop()
        r_set.add(t)
        l_num = len(set(left))

        r_num = len(r_set)
        if l_num == r_num:
            answer += 1
            equal = 1
        elif equal == 1 and l_num != r_num:
            break


    return answer

topping = [1, 2, 1, 3, 1, 4, 1, 2]

print(solution(topping))
