# B5002_도어맨

diff = int(input())

info = input()
people = []
for i in info:
    people.append(i)

stack = [people[0]]
p = 1
while stack:
    # if diff == 0:     # diff가 0일때는 없나봄 엌
    #     p += 1
    #     break
    if len(stack) == diff + 1:
        if p >= len(people) or stack[-1] == people[p]:
            break
        elif stack[-1] != people[p]:
            stack.pop()
            people[p-1], people[p] = people[p], people[p-1]
            p -= 1

    if p >= len(people):
        p += 1
        break

    if stack[-1] != people[p]:
        stack.pop()
        p += 1
    else:
        stack.append(people[p])
        p += 1

    if not stack:
        if p < len(people):
            stack.append(people[p])
            p += 1


print(p-1)