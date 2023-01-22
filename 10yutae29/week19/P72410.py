# P72410_신규 아이디 추천


def solution(new_id):


    # 1단계
    # id를 한글자 한글자 확인하며 대문자 알파벳일 경우
    # 소문자로 변환
    new_id = list(new_id)
    for idx in range(len(new_id)):
        if new_id[idx].isupper():
            new_id[idx] = new_id[idx].lower()
    new_id= ''.join(new_id)

    # 2단계 and 3단계
    # 알파벳, 숫자, -, _, .   만 alter 리스트에 넣어줌(나머지 제거)
    # 만약 alter의 마지막 원소가 '.'인데 그다음 id의 스펠링이 '.'이라면
    # '.'이 연속되지 않도록 alter에 추가하지 않음
    alter = []
    for spell in new_id:
        if spell == '.' and alter and alter[-1] == '.':
            pass
        elif spell.isalpha() or spell.isnumeric() or spell in ['-', '_','.']:
            alter.append(spell)
    new_id = ''.join(alter)

    # 4단계
    # 양쪽 끝의 '.'제거
    new_id = new_id.strip('.')

    # 5단계
    # id가 빈 문자열이라면 a를 추가해줌
    if new_id == '':
        new_id = 'a'

    # 6단계
    # 만약 id길이가 16이상이라면 15자 이후로는 전부 제거
    # 제거 후 마지막 문자가 '.' 이라면 제거
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')

    # 7단계
    # id가 2글자 이하라면 3글자가 될때까지 id의 마지막 문자 추가
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))