import sys
sys.stdin = open('input_B1966.txt')

'''
프린터를 돌려가며 하는 큐
우선순위가 있기 때문에 출력하는 순서에 주의하면서 진행
받은 리스트를 오름차순으로 정렬한 리스트를 만들어줘서 뽑아야 하는 순서를 지정하자
인덱스 값으로 있는 친구가 몇번째로 프린팅되는지 체킹을 해야함으로 원형큐를 이용
'''

T = int(input())
while T:
    N, idx = map(int, input().split())
    # 인풋으로 받은 문서들의 배열
    printer = list(map(int, input().split()))
    # 전체 문서들을 우선순위에 따라서 정렬을 해준다
    priority = sorted(printer)
    # 몇번째 인덱스의 문서가 출력이 되었는지 알려줄 기록지
    printed = [0]*N
    # 현재 프린터기 맨 앞에 있는 문서 번호를 나타낼 변수
    top = 0
    # 현재 출력이 되는 친구가 몇번째로 출력이 되는지 알려주는 변수
    cnt = 0
    # 우리가 알고자하는 문서가 출력이 될때까지 반복진행
    while not printed[idx]:
        # 반복문 탈출을 위한 조건
        checked = 0
        # 현재 우선적으로 뽑아야하는 문서의 번호
        prior = priority.pop()
        # 출력될때까지 반복
        while not checked:
            # 프린터기의 top이 우선적으로 뽑아야 하는 친구와 같고 그 친구가 아직 출력 안된 친구라면
            if printer[top] == prior and not printed[top]:
                # 출력하고
                printed[top] = 1
                # 몇번째 출력인지 기록하고
                cnt += 1
                # 반복 탈출 조건 설정
                checked = 1
            # 아직 아니라면 다음 친구로 넘어가자
            top = (top+1) % N
    print(cnt)
    T -= 1
