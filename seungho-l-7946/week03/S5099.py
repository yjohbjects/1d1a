# SWEA 5099 - 피자 굽기 (D3)

'''
Queue를 사용하는 이유
> 큐는 pop한 요소를 바로 append를 할 수 있음
> 따라서, 현재 피자 오븐처럼 원 형태의 회전문놀이가 가능함
> 돌아왔을때, pop해서 반감시키고
>> 값이 0일 경우, 새로운 요소를 append
>> 값이 0이 아닐 경우, 그대로 append
> 반복하여 마지막으로 남은 요소의 idx+1을 result로 반환하면 됨
'''