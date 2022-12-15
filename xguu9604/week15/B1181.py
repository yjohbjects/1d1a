import sys


'''
같은 방식의 머지 소트 진행
근데 단어간에도 그냥 대소 비교가 되는군요!
'''


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return

        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        tmp = []
        l, h = low, mid

        while l < mid and h < high:
            # 우선 단어 길이 비교해서 병합
            if len(arr[l]) < len(arr[h]):
                tmp.append(arr[l])
                l += 1
            elif len(arr[l]) > len(arr[h]):
                tmp.append(arr[h])
                h += 1
            # 길이가 같은 경우에
            else:
                # 단어의 사전 순서 비교하기
                if arr[l] < arr[h]:
                    tmp.append(arr[l])
                    l += 1
                else:
                    tmp.append(arr[h])
                    h += 1

        while l < mid:
            tmp.append(arr[l])
            l += 1

        while h < high:
            tmp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = tmp[i - low]

    return sort(0, len(arr))


N = int(sys.stdin.readline())
# 반복된 단어들이 있어서 집합으로 걸러내주기
arr = set()
for i in range(N):
    # rstrip() 안하면 \n까지 같이 딸려온다
    arr.add(sys.stdin.readline().rstrip())
# 걸러내기 작업 끝났으면 다시 리스트로
arr = list(arr)
merge_sort(arr)
for word in arr:
    print(word)