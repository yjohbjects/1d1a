def check_left(left, x, y):
    i = left[0]
    j = left[1]
    if i == x:
        return abs(j - y) * 2
    elif j == y:
        return abs(i - x) * 2
    elif abs(i - x) == 1 and abs(j - y) == 1:
        return 3
    else:
        t = abs(i - x)
        k = abs(j - y)
        if t > k:
            return (t - k) * 2 + k * 3
        else:
            return (k - t) * 2 + t * 3


def check_right(right, x, y):
    i = right[0]
    j = right[1]
    if i == x:
        return abs(j - y) * 2
    elif j == y:
        return abs(i - x) * 2
    elif abs(i - x) == 1 and abs(j - y) == 1:
        return 3
    else:
        t = abs(i - x)
        k = abs(j - y)
        if t > k:
            return (t - k) * 2 + k * 3
        else:
            return (k - t) * 2 + t * 3
#
#
# numbers = "1756"
# left = [1, 0]
# right = [1, 2]
# keyboard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
# branches = []
# answer = 0
#
# for k in range(len(numbers)):
#     for i in range(4):
#         for j in range(3):
#             if keyboard[i][j] == numbers[k]:
#                 weight_left = check_left(left, i, j)
#                 weight_right = check_right(right, i, j)
#                 if weight_right > weight_left:
#                     left = [i, j]
#                     answer += weight_left
#                 elif weight_left > weight_right:
#                     right = [i, j]
#                     answer += weight_right
#                 else:
#                     branches.append([left, [i, j], k, answer + weight_left])
#                     left = [i, j]
#                     answer += weight_left
#                 break
#
# while branches:
#     for branch in branches:
#         left = branch[0]
#         right = branch[1]
#         checkpoint = branch[2]
#         now_weight = branch[3]
#         for k in range(checkpoint+1, len(numbers)):
#             if now_weight >= answer:
#                 break
#             else:
#                 for i in range(4):
#                     for j in range(3):
#                         if keyboard[i][j] == numbers[k]:
#                             weight_left = check_left(left, i, j)
#                             weight_right = check_right(right, i, j)
#                             if weight_right > weight_left:
#                                 left = [i, j]
#                                 now_weight += weight_left
#                             elif weight_left > weight_right:
#                                 right = [i, j]
#                                 now_weight += weight_right
#                             else:
#                                 branches.append([left, [i, j], k, now_weight + weight_left])
#                                 left = [i, j]
#                                 now_weight += weight_left
#                             break
#         answer = min(now_weight, answer)
#         branches.pop(0)
numbers = "1756"
answer = 6 * 100000
keyboard = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
            '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '7': (2, 0), '8': (2, 1), '9': (2, 2), '0': (3, 1)}

weights = [answer] * 100001
def checking(i, left, right, weight):
    global answer
    if i == len(numbers):
        weights[i] = min(weights[i], weight)
        return

    if weights[i] and i:
        if weights[i] < weight:
            return
        else:
            weights[i] = weight

    target = keyboard[numbers[i]]
    left_finger = keyboard[left]
    right_finger = keyboard[right]

    if left_finger == keyboard[numbers[i]]:
        checking(i + 1, numbers[i], right, weight + 1)
    elif right_finger == keyboard[numbers[i]]:
        checking(i + 1, left, numbers[i], weight + 1)
    else:
        checking(i + 1, numbers[i], right, weight + check_left(left_finger, target[0], target[1]))
        checking(i + 1, left, numbers[i], weight + check_right(right_finger, target[0], target[1]))



checking(0, "4", "6", 0)
