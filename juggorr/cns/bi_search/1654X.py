import sys
sys.stdin = open('in.txt')

K, N = map(int, sys.stdin.readline().split())

lines = [int(sys.stdin.readline()) for _ in range(K)]

max_len = max(lines)
min_len = 1
# print(max_len, min_len)

answer = 0

# 최대길이 = 총 더한길이 // N => 달성할 수 없는 길이
# 최소길이 = 가장긴 길이 // N => 달성 가능
# 달성할 수 없는 길이도 탐색에 포함시켜야함?
# 그러면 탐색이 제대로 가능한지?
# 끼에에엑!!!!
# 최댓값을 다르게 설정하고 시작 => 그 최댓값을 구하려고 하는건데?

# 이분탐색으로 c를구하자 => c로 일일히 나눠보기 => 나눠서 N이 나올경우
# 해당 c를 l로 두고, 안나오면 r로두기?


def bi_search(l, r):
    
    while True:
        c = (l + r) // 2
        # print(c)
        # return
        # 세는거 초기화하고, 세보자구~
        counts = 0

        for line in lines:
            counts += line // c 

        if counts > N:
            l = c + 1
            continue
        
        elif counts < N:
            r = c - 1
            continue

        # 이분탐색으로 찾을 수 있는 값을 찾은 것.
        # 이값보다 클수있음 ok
        # 이값보다 작을수도 있음?
        else:
            return c
        

suspect = bi_search(min_len, max_len)

while True:
    # print(suspect)
    counts = 0

    for line in lines:
        counts += line // suspect

    # print(counts)

    if counts != N:
        break

    else:
        suspect += 1     
print(suspect - 1)