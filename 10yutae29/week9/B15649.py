# B15649_N과 M(1)

# 다음 과목평가의 중요도가 부분집합 -> 순열 -> 조합 순서
# import 사용 불가할 경우 대비맨


# n: 원소 리스트의 길이 N or len(elements) 4
# picked: 부분집합원소를 담을 리스트  처음엔 빈리스트로 입력됨 []
# to_pick: 목표로 하는 부분집합의 길이 M = 2
# elements: 부분집합을 뽑아낼 원소 리스트 [1, 2, 3, 4]
def permutation(n, picked, to_pick, elements):
    # 원하는 길이의 부분집합 picked를 만들었다면,
    # ans에 입력후 함수종료, 상위 함수로 복귀
    if to_pick == 0:
        # 이렇게 복사하지 않으면, 상위함수에서 pop 매서드로 인해 ans의 값도 pop됨
        result = picked[::]
        # ans에 부분집합 입력
        ans.append(result)
        # 함수 종료
        return

    # 부분집합 구하기
    for i in range(n):
        # i번째 원소가 picked에 입력되지 않았다면
        if elements[i] not in picked:

            # i번쨰 원소를 picked에 추가
            picked.append(elements[i])

            # 원소가 추가된 picked의 정보와
            # 목표로 하는 부분집합의 길이가 되기위한 목표치 to_pick-1
            # 을 정보로 담아 함수 재귀
            permutation(n, picked, to_pick - 1, elements)
            # 다른 경우의 수를 계산하기위해 pop해줌
            picked.pop()




# 1부터 N까지의 자연수 집합 만들거임
# 그중 길이가 M인 수열을 구할거임
# N = 4, M = 2
N, M = map(int,input().split())

# 부분집합을 뽑아낼 원소리스트
# [1, 2, 3, 4]
elements = list(range(1, N+1))

# 완성된 부분집합을 입력할 정답 리스트
# [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
ans = []

# 함수 실행후 ans 출력
permutation(N, [], M, elements)
for an in ans:
    print(f'{" ".join(list(map(str,an)))}')



'''
def permutation(n, picked, to_pick, elements):
    
    if to_pick == 0:       
        result = picked[::]       
        ans.append(result)       
        return

    
    for i in range(n):       
        if elements[i] not in picked:      
            picked.append(elements[i]) 
            permutation(n, picked, to_pick - 1, elements)     
            picked.pop()
'''