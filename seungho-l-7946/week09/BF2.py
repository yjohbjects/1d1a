def solution(answers):
    answer = []

    supo1 = [1, 2, 3, 4, 5] * 8
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4

    result = [0] * 3

    for i in range(len(answers)):
        if supo1[i % 5] == answers[i]:
            result[0] += 1
        if supo2[i % 8] == answers[i]:
            result[1] += 1
        if supo3[i % 10] == answers[i]:
            result[2] += 1

    max_r = max(result)

    for r in range(len(result)):
        if max_r == result[r]:
            answer.append(r + 1)

    return answer

print(solution([1, 2, 3, 4, 5]))
solution([1, 3, 2, 4, 2])