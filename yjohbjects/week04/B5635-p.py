import sys
from pprint import pprint

N = int(input())
birthday = []
for _ in range(N):
    name, dd, mm, yy = map(str, input().split())
    birthday.append([name, int(dd), int(mm), int(yy)])


birthday = sorted(birthday, key=lambda x:(x[3], x[2], x[1]))

print(birthday[-1][0]) # youngest
print(birthday[0][0]) # oldest