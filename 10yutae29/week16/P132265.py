# P132265_롤케이크 자르기

# Counter 쓰면 리스트의 원소 갯수를 {key = 원소 value: 갯수} 형태의 딕셔너리로 만들어준다
from collections import Counter

def solution(topping):
    answer = 0

    # 비교를 끝내버리기 위한 flag
    equal = 0

    # 왼쪽 set에 원소를 하나씩 넣어갈거임
    # 나중에 set의 길이로 비교함
    left = set()
    # 오른쪽엔 모든 토핑을 넣고 그 갯수를 센 딕셔너리를 만들어줌
    right = Counter(topping)

    # 토핑 돌면서
    for t in topping:
        # 왼쪽에 더해주고
        left.add(t)
        # 오른쪽의 토핑에서 갯수 -1 해줌
        right[t] -= 1

        # 만약 오른쪽 딕셔너리에서 토핑의 갯수가 0개라면 그 원소를 제거함
        if right[t] == 0:
            del right[t]

        # 양쪽 토핑 갯수 비교해서 같으면 answer +1
        if len(left) == len(right):
            answer += 1
            # 양쪽 토핑 갯수가 같은 구간에 들어섰다는 의미로 equal = 1
            equal = 1

        # 양쪽 토핑 갯수가 같은 구간이 끝나면 더이상 비교할 필요 없으므로 break
        elif equal == 1 and len(left) != len(right):
            break

    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]

print(solution(topping))


