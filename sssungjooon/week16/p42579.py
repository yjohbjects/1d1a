def solution(genres, plays):
    answer = []
		# 장르별 재생횟수 저장
    dic = {}
		# 앨범 상세 (노래별)
    album = {}
    # genres[i] = 고유번호가 i인 노래의 장르
    # plays[i] = 고유번호가 i인 노래가 재생된 횟수
    
    for i in range(len(genres)):
        if genres[i] not in dic:
            # 장르별 재생된 횟수 저장
            dic[genres[i]] = plays[i]
            # 이차원 배열 형태로 [재생 횟수, 고유 번호] 저장
            album[genres[i]] = [[plays[i], i]] 
        else:
            # 이미 있다면 장르에 재생 횟수 더하기
            dic[genres[i]] += plays[i] 
            album[genres[i]].append([plays[i], i]) 
            
    # items()함수를 사용하여 딕셔너리에 있는 키와 값들의 쌍으로 얻자
		# 키와 값이 쌍으로 나온다. (genres[i] , plays[i])
		# 1. 많이 재생된 장르 순으로 정렬하자
    dic = sorted(dic.items(), key=(lambda x:x[1]), reverse = True) 
    
    # 2. 많이 재생된 장르를 차례대로 탐색
		# 장르별 순회
    for genre in dic:
				# tmp에 장르별 노래들이 다 나옴 
        tmp = album[genre[0]]
        # 재생된 횟수를 기준으로 내림차순 정렬
        tmp = sorted(tmp, key=lambda x:x[0], reverse = True) 
        
        # 노래가 2개 이상이면 첫번째, 두번째 고유번호만 가져옴
        if len(tmp) > 1: 
            answer.append(tmp[0][1])
            answer.append(tmp[1][1])
        else:
            answer.append(tmp[0][1])
            
    return answer