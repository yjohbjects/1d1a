# P42579_베스트앨범

def solution(genres, plays):
    answer = []
    genres_info = {}

    # genres_info 딕셔너리에 각 장르를 key값으로 넣을것임
    # 각 key에 대한 value 값으로 [총 재생횟수, 재생횟수 제일큰 노래 고유번호, 재생횟수 두번쨰로 큰 노래 고유번호] 넣음
    for i in range(len(genres)):
        genre = genres[i]
        play_time = plays[i]

        # 만약 장르정보가 이미 genres_info에 들어갔으면
        if genre in genres_info:
            # 해당 장르 재생횟수 더해줌
            genres_info[genre][0] += play_time

            # play_time이 기존 장르의 최다 재생수보다 크다면
            # 기존 최다 재생수 음악 -> 두번째로 많은 재생 수 음악
            # 현재 확인하는 음악 -> 최다재생수 음악
            if play_time > plays[genres_info[genre][1]]:
                genres_info[genre][2] = genres_info[genre][1]
                genres_info[genre][1] = i
            
            # 장르에 두번째로 재생횟수가 높은 음악이 존재하고, play_time이 두번째 재생횟수보다 많거나 or
            # 아직 두번째로 재생횟수가 높은 음악이 입력되지 않았다면
            # 두번째로 재생횟수가 높은 음악 -> 현재 확인하는 음악
            elif (genres_info[genre][2] >= 0 and play_time > plays[genres_info[genre][2]]) or genres_info[genre][2] == -1:
                genres_info[genre][2] = i
        
        # 딕셔너리에 장르에 대한 정보가 입력되지 않았다면 데이터 추가
        else:
            genres_info[genre] = [play_time, i, -1]

    # 장르의 키값을 장르별 재생횟수 내림차순으로 정렬한 리스트
    sorted_keys = sorted(genres_info, key= lambda k: genres_info[k][0], reverse=True)

    # 재생횟수가 큰 장르의 음악부터 answer에 입력할것
    for key in sorted_keys:
        first, second = genres_info[key][1:]
        # 장르 데이터가 있으면 최소 1곡은 있으니 frist노래는 바로 입력
        answer.append(first)
        # 만약 노래가 2개이상이라면 (노래가 1곡뿐이면 second 값이 -1 임)
        # second 노래 입력
        if second != -1:
            answer.append(second)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))