def solution(brown, yellow):
    answer = []
    
    # 총 면적
    total = brown + yellow
    
    # 가로, 세로 최소길이 = 3
    # 3부터 1씩 증가시키면서 total을 나눌 수 있는 숫자가 나오면
    # answer에 넣고, 내림차순으로 정렬
    val = 3
    
    while True:
        # 나누어 떨어지면
        if total % val == 0:
            # (가로길이 - 2) * (세로길이 - 2) == yellow면
            # answer에 넣어주기
            if (val - 2) * (total // val - 2) == yellow:
                answer.append(val)
                answer.append(total // val)
                break
            else:
                val += 1
        # 나누어 떨어지지 않으면 val 값 올려주기
        else:
            val += 1
            
    # answer 내림차순 정렬해주기
    answer.sort(reverse=True)
    return answer