# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
# 10 1 9 2 8 3 7 4 6 5
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

# 첫 줄에 테스트 케이스 개수 T (1 <= T <= 50)
T = int(input())

# 테스트 케이스 개수만큼 반복하고, 
# 정수 입력 값을 받고, 정렬할 숫자들을 리스트로 만든다
for test_num in range(1, T+1):
    N = int(input())
    Num_list = list(map(int, input().split()))
    # 특별한 정렬 후 다시 넣을 리스트 Sort_list를 만들자
    # 이때 
    Sort_list = [0]*N
    # 남은 것 중 가장 큰 수 구하기
    for i in range(N//2) :                      # 반복문을 통해서
        Sort_list[i*2] = max(Num_list)          # 주어진 숫자 리스트의 최댓값을 홀수 번째로 바꾼다
        Num_list.pop(Num_list.index(max(Num_list))) # 그리고 나서 pop을 통해 리스트에서 해당 최댓값을 제거한 후 다시 반복

    # 마찬가지로 남은 것 중 가장 작은 값 구하기
    for i in range(N//2) :
        Sort_list[i*2+1] = min(Num_list)
        Num_list.pop(Num_list.index(min(Num_list)))

    # 앞에 테스트 회차 번호 출력
    print('#%s'%test_num, end=' ')
    # 다시 정렬된 Sort_list의 요소 값들을 차례대로 10개까지 출력
    for i in range(10) :
        print(Sort_list[i], end=" ")
    print()