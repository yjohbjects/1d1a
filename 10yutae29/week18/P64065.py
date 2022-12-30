# P64065_튜플

def solution(s):
    answer = []

    # 숫자와 ','로만 이루진 원소를 갖는 리스트를 갖기위해 스플릿
    # ['1,2,3', '2,1', '1,2,4,3', '2']
    nums = s[2:-2].split('},{')

    # 위의 리스트를 str에서 int형 숫자를 담은 리스트를 담은 리스트로 변경
    for n in range(len(nums)):
        nums[n] = list(map(int,nums[n].split(',')))
    # 리스트의 길이에 따라 정렬
    # [[2], [2, 1], [1, 2, 3], [1, 2, 4, 3]]
    nums.sort(key=lambda x:len(x))

    # answer에 첫번째 원소 입력
    answer.append(nums[0][0])

    # 이후 1번 인덱스부터 확인
    # set의 차집합을 활용해 n번째 숫자를 찾아서 answer에 입력
    for n in range(1, len(nums)):
        answer.append((set(nums[n]) - set(nums[n - 1])).pop())

    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
