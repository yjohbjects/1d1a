import sys
sys.stdin = open("4880.txt")

# 사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다.
# 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
# 1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다.
# 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
# 그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.
# 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.
# 다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다.
# 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.
# N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.

# 가위바위보 조건부터 만들자 (가위는 1, 바위는 2, 보는 3)
def win(student, A, B):
    # win이라는 함수는 관찰하는 값이 인덱스이므로 인덱스만을 반환하게 한다.
    # 조건은 리스트의 해당 인덱스의 값으로 비교한다.
    # A가 인덱스가 B보다 작다

    # A가 가위를 냈을 때
    if student[A] == 1:
        # B가 같은 가위를 내거나 (B가 인덱스 많으니 졌다)
        # B가 보를 내면 A가 이긴다.
        if student[B] == 1 or student[B] == 3:
            return A
        else:
            return B
    # A가 바위를 냈을 때
    elif student[A] == 2:
        # B가 보를 내면 B가 이긴다.
        if student[B] == 3:
            return B
        # B가 바위를 내도 인덱스 때문에 지고, B가 가위를 내도 가위바위보 때문에 진다.
        else:
            return A
    # 위의 조건을 빼고 나머지 조건 중 B가 가위를 내는 경우를 제외하고는 (A, B 둘다 가위인 경우는 위에서 A가 이긴다고 언급)
    # A가 이긴다.
    else:
        if student[B] == 1:
            return B
        else:
            return A

# 카드게임
def cardgame(student, start, end):
    # 인덱스 값들만 움직이므로 해당 인덱스가 같아질 때, 즉 한 요소만 남았을 때 인덱스를 반환한다.
    if start == end:
        return start
    # 문제에 조건이 나와있으므로 해당 조건을 이용해 두 그룹으로 나눈다
    first = cardgame(student, start, (start + end) // 2)
    second = cardgame(student, (start + end) // 2 + 1, end)
    # 최종적으로 두 그룹 중 이긴 쪽을 출력한다.
    return win(student, first, second)

# 테스트 케이스 시작
T = int(input())

for test_count in range(1, T+1):
    # 인원 수 N명 인풋값 받기
    N = int(input())
    # N명의 학생들의 카드 입력받기
    students = list(map(int, input().split()))
    result = cardgame(students, 0, N - 1)

    # result는 인덱스값을 나타내므로 +1해준다.
    print(f"#{test_count} {result + 1}")