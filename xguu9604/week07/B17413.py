import sys
sys.stdin = open('input_B17413.txt')

T = int(input())
while T > 0:
    strings = input()
    new_words = []
    new_word = []
    stack = 0
    for string in strings:
        if stack:
            if string == '>':
                new_word.append(string)
                new_words.append(new_word)
                new_word = []
                stack = 0
            else:
                new_word.append(string)
        else:
            if string == '<':
                if new_word:
                    new_words.append(new_word)
                    new_word = ['<']
                    stack = 1
                else:
                    new_word = ['<']
                    stack = 1
            elif string == ' ':
                new_words.append(new_word)
                new_words.append([' '])
                new_word = []
            else:
                new_word.append(string)

    if new_word:
        new_words.append(new_word)
    answers = []
    for word in new_words:
        if word[0] == '<':
            answers.append(word)
        elif word == [' ']:
            answers.append(word)
        else:
            answers.append(word[::-1])
    for answer in answers:
        for char in answer:
            print(char, end='')
    print()
    T -= 1