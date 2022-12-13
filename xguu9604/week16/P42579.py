def solution(genres, plays):
    answer = []
    # 전체 곡의 수
    N = len(plays)
    # 장르별로 재생된 횟수를 기록하기 위한 딕셔너리
    genre_dict = {}
    # 장르별로 순회를 하면서 각 장르의 원소를 생성
    for genre in genres:
        genre_dict[genre] = [0, False]

    # 전체 곡을 순회하면서 그 곡이 속한 장르에 해당 곡의 재생 횟수를 더해줌
    for i in range(N):
        genre_dict[genres[i]][0] += plays[i]

    # 장르의 개수
    M = len(genre_dict)

    # 전체 장르 횟수 만큼 반복
    while M:
        # 가장 많이 들은 횟수
        most_heard = 0
        # 가장 많이 들은 장르
        most_genre = ''
        for info in genre_dict:
            # 아직 확인한 장르는 아니고 현재 횟수 중에서 제일 많이 재생된 장르 선택하기
            if genre_dict[info][0] > most_heard and not genre_dict[info][1]:
                most_heard = genre_dict[info][0]
                most_genre = info
        # 해당 장르가 선택되었음을 체킹
        genre_dict[most_genre][1] = True
        # 고려할 곡들을 담아줄 리스트
        to_think = []
        # 현재 선택된 장르들을 고려대상에 추가
        for i in range(N):
            if most_genre == genres[i]:
                to_think.append((plays[i], i))
        # 해당 장르의 곡을 재생횟수대로 정렬하고 그 다음 순서로 곡 고유번호로 정렬
        to_think.sort(key=lambda x: (-x[0], x[1]))
        # 해당 장르의 곡이 2곡 이상이라면 2곡만 추출
        if len(to_think) >= 2:
            for j in range(2):
                answer.append(to_think[j][1])
        # 한곡따리면 한곡만 넣기
        else:
            answer.append(to_think[0][1])
        M -= 1
    return answer