word = input()

post = []
post.append(word[-1])
for i in range(len(word) - 2, -1, -1):
    post.append(word[i] + post[-1])

post.sort()
for i in post:
    print(i)