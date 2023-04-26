import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 절단기의 높이 구하기 문제
# 절단기 높이의 최소값 = 0 /  최대값 = 가장긴 나무 크기
# 절단기 = 0 => 나무 다베어서 가져감 => sum(trees)
# 절단기 = max(trees) => 나무 하나도 못 베어감 => 0

l, r = 0, max(trees)

# 나무 탐색하면서 잘라서 얻는 나무 길이 구하는 함수
def got_tree(list, h):
    total = 0

    for tree in list:
        if tree > h:
            total += tree - h

    return total

# 이분 탐색이 끝나는 조건 = 좌우 역전 세카이
while l <= r:
    c = (l + r) // 2

    # 해당 높이로 자르면 더 많이 자를 경우
    # 높이를 조금더 높여도 된다
    if got_tree(trees, c) < M:
        r = c - 1
        
    # 현재 높이로 원하는 만큼 나무를 얻을 수 없으면 벌목기를 더 낮춰야 한다
    else:
        l = c + 1

print(r)