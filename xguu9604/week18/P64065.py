
'''
그냥 전부다 쪼개고 리스트로 바꾸고 중복찾아서 튜플 생성하기
이게 맞는건지 의심
'''

def solution(s):
    answer = []
    tuples = []

    # 튜플 한개씩 저장할 친구
    checker = ''
    i = 1

    # 전체 인풋의 길이를 순회하자
    while i < len(s):
        # 닫는 괄호 나오면
        if s[i] == '}':
            # 완성된 튜플 넣어주고
            checker += s[i]
            tuples.append(checker)
            # 두칸을 건너뛸 예정
            i += 1
            # 체커 초기화
            checker = ''

        # 그 외의 경우는 그냥 더해주기
        else:
            checker += s[i]

        # 반복 한번 돌면 인덱스 +=1
        i += 1

    # 이번엔 만든 튜플들을 리스트로 받을 전체 리스트
    lsts = []

    # 튜플들을 순회하면서
    for tup in tuples:
        # 끝에 괄호들 쳐내고 ,로 나눈 리스트 생성
        lst = list(map(int, tup[1:-1].split(',')))
        lsts.append(lst)

    # 리스트들 길이 순서대로 정렬
    lsts.sort(key=lambda x: len(x))

    # 중복 체크해줄 집합
    setter = set()

    # 전체 리스트들을 순회하면서
    for lst in lsts:
        for i in lst:
            # 해당 원소가 중복이 아니라면 추가하기!
            if i not in setter:
                setter.add(i)
                answer.append(i)
                break

    return answer