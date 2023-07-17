N = int(input())

fibs = [0, 1]

# 메모이제이션 dp 무슨관계였지..?
# 메모이제이션은 dp의 구현방식
# 시간을 희생하는대신 메모리를 활용해서 채운다!
def nazi(n):
    # n이 2보다 작은 수라면 그대로 반환
    if n < 2:
        return fibs[n]
    
    # n이 2보다 이상이라면
    else:
        # 이미 fibs[n]이 있다면
        if len(fibs) > n:
            return fibs[n]
        
        # 없다면 해당 숫자까지 만들기
        else:
            for i in range(len(fibs), n + 1):
                fibs.append(fibs[i - 1] + fibs[i - 2])

            return fibs[n]
    
print(nazi(N))