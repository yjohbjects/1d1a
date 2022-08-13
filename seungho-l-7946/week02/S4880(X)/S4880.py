# 토너먼트 카드게임
import sys
sys.stdin = open("onedayonealgorithm/week02/S4880/input.txt")

def card_rsp(p1, v1, p2, v2):

    if v1 == 1:
        if v2 == 1:
            return p1
        elif v2 == 2:
            return p2
        elif v2 == 3:
            return p1
    elif v1 == 2:
        if v2 == 1:
            return p1
        elif v2 == 2:
            return p1
        elif v2 == 3:
            return p2
    elif v1 == 3:
        if v2 == 1:
            return p2
        elif v2 == 2:
            return p1
        elif v2 == 3:
            return p1
        
def grouping(n1, n2):
    start = n1
    end = n2

    if (end-start) == 1:
        return start
    elif (end-start) == 2:
        return start

    if end % 2 == 0:
        middle = int(end/2)
        grouping(start,middle)
        grouping(middle+1,end)
    else:
        middle = int((start + end)/2)
        grouping(start,middle)
        grouping(middle+1,end)

num = int(input())

for i in range(1, num+1):

    N = int(input())
    test = list(map(int, input().split()))

    print(grouping(1, N))

    
    # result = 0
    
    # print(f'#{i} {result}')