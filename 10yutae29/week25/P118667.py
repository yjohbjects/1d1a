# P118667_두 큐 합 같게 만들기
# from collections import deque

def solution(queue1, queue2):
    answer = -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = (sum1 + sum2)//2
    a, b, length = 0, 0, len(queue1)
    while sum1!=sum2 and a<2*length and b<2*length:
        if sum1<total:
            sum1 += queue2[b]
            sum2 -= queue2[b]
            queue1.append(queue2[b])
            b += 1
        else:
            sum1 -= queue1[a]
            sum2 += queue1[a]
            queue2.append(queue1[a])
            a+= 1
    if sum1==total:
        answer = a+b
    return answer




print(solution([3, 2, 7, 2],[4, 6, 5, 1]))