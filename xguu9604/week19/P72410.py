'''
그냥 요구하는 조건 하나씩 순서대로 구현하기
'''

def solution(new_id):
    # 1. 대문자 소문자로 고쳐주기
    new_id = new_id.lower()

    # 문자열이면 고치기 불편해서 리스트로 변환하기
    id_lst = list(map(str, new_id))

    # 2. 사용 불가능한 특수문자 지우기
    # i: 인덱스 값
    i = 0
    # 끝까지 순회하자
    while i < len(id_lst):
        # 알파벳이면 다음 친구로
        if id_lst[i].isalpha():
            i += 1
        # 숫자면 다음 친구로
        elif id_lst[i].isdigit():
            i += 1
        # 사용 가능한 특수문자면 다음으로
        elif id_lst[i] in '-_.':
            i += 1
        # 위에서 전부 걸러졌으면 못쓰는 친구이므로 pop
        # pop하면 인덱스가 어차피 당겨져서 인덱스 조정이 필요없음
        else:
            id_lst.pop(i)

    # 3. 중복되는 . 지우기
    i = 0
    dup = 0
    # 끝까지 순회하면서
    while i < len(id_lst):
        # 만약 .을 만난경우
        if id_lst[i] == '.':
            # 중복점이라면 현재 .을 pop
            if dup:
                id_lst.pop(i)
            # 처음 만난 .이면 중복 체크를 해주고 다음으로
            else:
                dup = 1
                i += 1

        # .이 아닌경우 중복 해제후 다음으로
        else:
            dup = 0
            i += 1

    # 아이디가 공란이 아닌경우
    if id_lst:
        # 4. 맨 앞의 점 빼기
        if id_lst[0] == '.':
            id_lst.pop(0)

    # 4. 맨뒤에 점도 똑같이 빼기
    if id_lst:
        if id_lst[-1] == '.':
            id_lst.pop()

    # 5. 아이디가 공백이 되면 'a'를 넣어주자
    if not id_lst:
        id_lst.append('a')

    # 6. 아이디가 15보다 길어지면 15개만 앞에서 자르기
    if len(id_lst) > 15:
        id_lst = id_lst[:15]
        # 맨뒤가 .이면 빼주기
        if id_lst[-1] == '.':
            id_lst.pop()

    # 7. 아이디가 3보다 작으면 3이 될때까지 맨 뒤 문자 계속 뒤에 추가
    while len(id_lst) < 3:
        id_lst.append(id_lst[-1])

    return ''.join(id_lst)