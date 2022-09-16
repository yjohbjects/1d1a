T = int(input())
line = list(map(str, input()))
stack_m = 0
stack_w = 0
swap = 0
top = 0
while swap < 2:
    if abs(stack_m-stack_w) < T:
        if line[top] == 'M':
            stack_m += 1
        else:
            stack_w += 1
    elif abs(stack_m-stack_w) == T:
        if stack_m > stack_w:
            if line[top] == 'M':
                swap += 1
            elif line[top] == 'W' and swap:
                stack_w += 1
                stack_m += 1
                swap -= 1
            else:
                stack_w += 1
        elif stack_w > stack_m:
            if line[top] == 'W':
                swap += 1
            elif line[top] == 'M' and swap:
                stack_w += 1
                stack_m += 1
                swap -= 1
            else:
                stack_m += 1
    if top == len(line)-1:
        break
    top += 1
print(stack_m+stack_w)

