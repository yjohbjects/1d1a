def solution(m, n, puddles):
    # 해당 지형에 맞는 배열 생성
    arr = [[0] * (m + 1) for _ in range(n + 1)]

    # 왼쪽 벽으로 가는 경우의 수는 1개뿐
    for i in range(1, n + 1):
        arr[i][1] = 1
    
    # 천장으로 가는 경우의 수도 1개뿐
    for j in range(1 , m + 1):
        arr[1][j] = 1

    # 웅덩이들을 순회하면서 웅덩이 체크하기        
    for puddle in puddles:
        arr[puddle[1]][puddle[0]] = -1
        
        # 이 녀석들이 엣지 케이스!!
        # 웅덩이들 중에서 왼쪽 벽이나 천장에 붙어있는 웅덩이가 있을 수 있다
        # 그 경우에 그 웅덩이 뒤에 존재하는 길들은 갈 수 없는 길이된다
        # 그래서 그 뒤에 지역들을 0으로 초기화 시켜줘야 순회하면서 그 구역의 경우의 수를 빼주게 되는 것
        if puddle[1] == 1:
            for j in range(puddle[0], m + 1):
                arr[1][j] = 0
        
        elif puddle[0] == 1:
            for i in range(puddle[1], n + 1):
                arr[i][1] = 0
            
    # 웅덩이까지 체크 다했으면 경우의 수를 세어주러 가자
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            # 만약 현재 지점이 웅덩이면 못 오는 길이니까 0으로 초기화
            if arr[i][j] == -1:
                arr[i][j] = 0
            # 그 외의 경우들은 위에서 오는 경우와 왼쪽에서 오는 경우의 수를 더해주자
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
            
            # 근데 현재 값이 조건의 저 숫자보다 크면 숫자를 줄여주자
            # 너무 큰 수들끼리 더해서 숫자 크기 제한을 넘어가기도 한다더라
            if arr[i][j] > 1000000007:
                arr[i][j] = arr[i][j] % 1000000007
    
    print(arr)
    # 맨 끝에 학교 좌표가 전체의 경우의 수가 된다.
    return arr[n][m]