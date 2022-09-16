# B5002 도어맨

memory = int(input())
ppls = input()

cnt = 0
stack = []
for ppl in ppls:
    # 대기 인원이 있는 경우
    if stack and stack[-1] == 'wait-up':
        if stack[-2] == ppl: # 또 동성이 들어가?
            stack.pop() # 대기 제거
            break
        else: # stack[-2] != ppl: 이성이닷!
            stack[-1] = 'M'
            cnt += 1 # 대기하던 사람 & 이성이 들어간닷
        
    # stack이 비어있으면 추가
    if not stack:
        stack.append(ppl)
        cnt += 1

    # 성비가 맞는 사람이 오면 pop
    elif stack[-1] != ppl:
        stack.pop()
        cnt += 1

    # 성비가 안맞아!
    elif stack[-1] == ppl:
        # 동성이 들어가려는데, 기억력 소진한 경우
        if len(stack) == memory:
            stack.append('wait-up')
        # 동성이 들어가려는데, 기억력이 되는 경우 append
        else:
            stack.append(ppl)
            cnt += 1
    # print(stack, cnt)

print(cnt)
