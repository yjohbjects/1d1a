# P42842 카펫

def solution(brown, yellow):
    # brown + yellow 블록의 수
    # 공약수를 구해서 계산식이 맞는지 완전탐색

    block_num = brown + yellow
    for i in range(1, block_num // 2):
        if block_num % i == 0:
            if i < block_num // i:
                x = block_num // i
                y = i
            else:
                x = i
                y = block_num // i
            
            if block_num - ((x + y) * 2 - 4) == yellow:
                answer = [x, y]

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))