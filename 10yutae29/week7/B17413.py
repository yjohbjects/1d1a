# B17413 단어 뒤집기2

S = input()
ans = ''
stack = []
status = 0
for s in S:
    if s == '<':
        status = 1
    elif s == ' ' and status == 0:
        status = 2
    elif s == '>':
        status = 0
        ans += s
        continue

    if status == 0 or (status == 2 and s.isalnum()):
        stack.append(s)
    elif status == 1 or status == 2:
        while stack:
            ans += stack.pop()
        ans += s
while stack:
    ans += stack.pop()
print(ans)