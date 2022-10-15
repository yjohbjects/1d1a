import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
to_spend = []
for _ in range(N):
    to_spend.append(int(input()))
left = min(to_spend)
right = sum(to_spend)
min_withdrawal = right
while True:
    mid = (left + right) // 2
    in_hand = mid
    withdrawal = 1
    for spend in to_spend:
        # 여기 if문 추가로 문제 정답.. 왜일까?
        if spend > mid:
            withdrawal += M
            break
        if spend > in_hand:
            in_hand = mid - spend
            withdrawal += 1
        else:
            in_hand -= spend
    if withdrawal > M:
        left = mid + 1
    elif withdrawal <= M:
        right = mid - 1
        min_withdrawal = min(mid, min_withdrawal)
    if left > right:
        break
print(min_withdrawal)