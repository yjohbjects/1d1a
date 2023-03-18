def solution(numbers):
    # 문제에서 주어진 배열의 길이
    N = len(numbers)
    # 우선 배열의 길이에 맞게 답 배열을 선언해주자
    answer = [-1] * N
    # 지금까지 지나온 숫자들을 기록해줄 stack
    # 선입선출 방식으로 가장 가까운 숫자부터 비교를 해주자
    stack = []
    # 뒤에서부터 배열을 탐색하면서 크기를 비교
    for i in range(N-1, -1, -1):
        # 현재 스택에 추가된 값이 없다면 비교값이 없다는 의미
        if not stack:
            # 현재 배열의 값을 스택에 추가하고 끝
            stack.append(numbers[i])
        else:
            # 스택을 전부 확인해보자
            while stack:
                # 스택의 top 값이 현재 배열값보다 크다면 
                if numbers[i] < stack[-1]:
                    # 지금 찾고자 하는 조건에 부합하는 값이므로 답지 교체
                    answer[i] = stack[-1]
                    # 그리고 지금 확인한 배열의 값도 스택에 push
                    stack.append(numbers[i])
                    # 더 확인할 필요 없으니 반복 종료
                    break
                # 그 외의 경우는 top값이 필요 없으니 빼고 다음으로
                else:
                    stack.pop()
            # 스택이 빈 경우에는
            else:
                # 현재 배열값만 스택에 push하고 끝
                stack.append(numbers[i])
                
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
