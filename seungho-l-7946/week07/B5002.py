# BAEKJOON 5002 - 도어맨 (S1)

'''
문제
1) 클럽에 있는 남자와 여자의 차이를 계산하는데, 한계값이 있음.
2) 유도리있게 두번째사람까지 입장이 가능함.
3) 클럽내의 인원 수를 구하라.

풀이
** 두번째 사람 입장시킬 경우에는 첫번째 사람을 tmp값으로 지정
1) 차이값이 한계값인 경우
1-1) tmp 값이 비어있는 경우
1-1-1) top 값이랑 같을 경우 tmp 값으로 지정하고 continue
1-1-2) top 값이랑 같지 않을 경우 2-1 처럼 진행
1-2) tmp 값이 비어있지 않은 경우
1-2-1) 다음사람이 tmp 값과 같은 경우 종료
1-2-2) 다음사람이 tmp 값과 다르다면, tmp와 human 모두 append 하고 tmp 값 초기화
2) 차이값이 한계값보다 작은 경우
2-1) 여자면 cnt + 1, 남자면 cnt - 1 해서 stack에 append

입력
1) 첫째줄에 기억할 수 있는 가장 큰 차이 X가 주어짐.
2) 둘째줄에는 줄을 서 있는 순서가 주어짐.
3) W는 여성, M은 남성이며 가장 왼쪽이 가장 앞임.

출력
1) 클럽에 있는 사람 수의 최댓값을 출력
'''

import sys

sys.stdin = open('B5002.txt')

# input
X = int(input())
waiting = input()
stack = []
cnt = 0
tmp = ''
for human in waiting:
    if abs(cnt) == X:
        if not tmp:
            if stack[-1] == human:
                tmp = human
                continue
            else:
                stack.append(human)
                if cnt < 0:
                    cnt += 1
                else:
                    cnt -= 1
        else:
            if human == tmp:
                break
            else:
                stack.append(human)
                stack.append(tmp)
                tmp = ''
    else:
        if human == 'W':
            stack.append(human)
            cnt += 1
        else:
            stack.append(human)
            cnt -= 1

result = len(stack)

# output
print(result)