import sys

sys.stdin = open('2.txt')

nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

result = []
stack = []
while nodes:
    if not stack:
        stack.append(nodes.pop(0))
    else:
        if stack[-1] < nodes[0]:
            tmp = nodes.pop(0)
            while stack[-1] < tmp:
                result.append(stack.pop())
                if not stack:
                    break
            tmp2 = result.pop()
            result.append(tmp)
            result.append(tmp2)
        else:
            stack.append(nodes.pop(0))


print(result)