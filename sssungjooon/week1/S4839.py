# 코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
# 예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
# 찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
# A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
# 책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

# 테스트 케이스 개수 T
T = int(input())

# 테스트 시행 수만큼 전체 쪽수 P, A와 B가 각각 찾을 쪽 번호를 대입
for test_num in range(1,T+1):
    P, A, B = map(int, input().split())
    countA = 0
    countB = 0
    left = 1
    right = P
    # A가 찾을 때 중간 페이지 c와 left right가 같은지 확인하는 조건문 만듦
    while True :
        c = int((left+right)/2)
        countA += 1
        if c == A:  # 중간 페이지 c가 A가 찾으려는 페이지와 같다면 조건문 종료
            break
        elif c < A: # 중간 페이지 c가 찾으려는 페이지보다 작다면 (펼쳤을 때 오른쪽 면에 찾으려는 페이지가 있다)
            left = c # 현재의 중간 페이지가 왼쪽 기준 페이지가 된다.
        else :          # 그 밖의 다른 케이스 (펼쳤을때 왼쪽 면에 찾으려는 페이지가 있다)
            right = c   #현재의 중간 페이지가 오른쪽 기준 페이지가 된다.

    # 마찬가지로 B가 찾을 때도 똑같이 만들어 준다.
    left = 1
    right = P
    while True :
        c = int((left+right)/2)
        countB += 1
        if c == B:
            break
        elif c < B:
            left = c
        else :
            right = c

    # 누가 빨리 찾아서 이겼는지 출력하므로 countA와 countB를 비교하여 출력하는 조건문을 만든다
    if countA == countB :
        print("#%d %d"%(test_num, 0))  # 비기면 0 출력
    elif countA > countB :
        print("#%d %s"%(test_num, 'B'))
    else :
        print("#%d %s"%(test_num, 'A'))