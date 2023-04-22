tc = int(input())

for _ in range(tc):
    answer = input()
    answer = '**' + answer.replace(' ', '**') + '**'
    # print(answer)


    while True:
        animal = input()

        if animal == 'what does the fox say?':
            answer = answer.replace('**', ' ')
            print(answer.strip())
            break

        else:
            sound = list(animal.split(' '))[2]
            answer = answer.replace('*' + sound + '*', '') 
