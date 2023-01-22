starter = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
r1 = '"재귀함수가 뭔가요?"'
r2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
r3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
r4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
rf = '"재귀함수는 자기 자신을 호출하는 함수라네"'
answer = '라고 답변하였지.'

def prof(N):
    global cnt
    space = ('_' * 4) * cnt

    # 해답에 도달했을 경우
    if cnt == N:
        print(space + r1)
        print(space + rf)
        print(space + answer)
    # 아직 해답을 찾고있는 경우
    else:
        # 재귀의 제일 처음일 경우
        if cnt == 0:
            print(starter)
        # 일반적으로 프린트 되는 답
        print(space + r1)
        print(space + r2)
        print(space + r3)
        print(space + r4)
        cnt += 1
        prof(N)
        print(space + answer)

N = int(input())
cnt = 0
prof(N)