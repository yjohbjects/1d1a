N = input()
F = int(input())

for i in range(100):
    N = list(N)
    N.pop()
    N.pop()
    N = ''.join(N)

    if i < 10:
        N += '0'+str(i)

        if int(N) % F == 0:
            print(f'0{i}')
            break
    else:
        N += str(i)
        
        if int(N) % F == 0:
            print(i)
            break
