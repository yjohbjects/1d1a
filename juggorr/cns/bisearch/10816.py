import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
ns = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().split()))


ns_dict = {}
for n in ns:
    if n in ns_dict:
        ns_dict[n] += 1
    else:
        ns_dict[n] = 1

for m in ms:
    result = ns_dict.get(m)

    if result == None:
        print(0, end=' ')
        
    else:
        print(result, end=' ')