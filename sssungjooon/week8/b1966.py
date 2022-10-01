T = int(input())

for test_count in range(T):
    # 문서의 개수 N, 궁금한 문서는 M번째 (0번부터)
    N, M = map(int,input().split())
    0 <= M < N
    importance = list(map(int,input().split()))
    # 순서만 저장하는 리스트
    order = [i for i in range(N)]
    # 뽑아낸 카운트
    count = 0

    while importance:
        # 제일 앞의 문서가 가장 중요도가 높은 문서라면
        if importance[0] == max(importance):    
            count += 1
            # 근데 그게 찾으려는 M 번째 문서라면
            if order[0] == M :
                print(count)
                break
            importance.pop(0)
            order.pop(0)
        else:
            importance.append(importance.pop(0))
            order.append(order.pop(0))