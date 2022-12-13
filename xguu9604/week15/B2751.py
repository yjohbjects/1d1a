import sys

'''
머지 소트 갈겨잇!
'''


def merge_sort(arr):
    # 일단 반갈죽하는 함수
    def sort(low, high):
        # 원소가 한개인 경우는 나눌 수 없응께 끝
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        # 위에서 일단 다 나눴으면 합치자
        merge(low, mid, high)

    # 이건 합치는 함수
    def merge(low, mid, high):
        # 작은 쪽의 포인터와 큰 쪽의 포인터
        l, h = low, mid
        # 분류한 친구들 임시 보관소
        tmp = []
        # 한쪽이라도 전부 순회할때까지
        while l < mid and h < high:
            # 비교해서 작은거 넣기
            if arr[l] < arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1

        # 남아있는 친구들 처치
        while l < mid:
            tmp.append(arr[l])
            l += 1

        while h < high:
            tmp.append(arr[h])
            h += 1

        # tmp에 전부 다 채웠으면 원본을 바꾸는 작업
        for i in range(low, high):
            # low와 high는 원본의 인덱스가 그대로지만
            # tmp는 0번부터 시작이므로 그 인덱스 위치를 맞춰서 원본을 바꿔주자
            arr[i] = tmp[i - low]

    # 이게 merge_sort() 함수의 전부
    return sort(0, len(arr))


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
merge_sort(arr)
for i in range(N):
    print(arr[i])
