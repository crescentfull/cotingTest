def solution(line):
    # 모든 직선 쌍에 대해 교점을 구함
    points = set() #교점
    n = len(line) #직선갯수
    
    for i in range(n): # 첫번째 직선 선택
        A, B, C = line[i]
        for j in range(i + 1, n): # 두번째 직선 선택
            D, E, F = line[j]
            
            denominator = A * E - B * D #분모
            if denominator == 0:
                continue  # 평행하거나 일치하는 직선, 분모가 0이면 교점이 없으므로 건너뜀
            
            #분자계산, 공식 그대로
            x_numerator = B * F - C * E
            y_numerator = C * D - A * F
            
            if x_numerator % denominator == 0 and y_numerator % denominator == 0:
                x = x_numerator // denominator # x값이 정수인지 확인
                y = y_numerator // denominator # y값이 정수인지 확인
                points.add((x, y)) # 정수라면 (x,y)를 points 집합 (set)에 추가
    
    if not points:
        return []
    
    # 좌표 범위 찾기, 찾은 (x,y) 좌표에서 가장작은 x,y와 가장큰 x,y값을 구한다
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)
    
    # 격자판 생성
    width = max_x - min_x + 1 #가로
    height = max_y - min_y + 1 #세로
    grid = [['.'] * width for _ in range(height)] #빈공간찍기
    
    # 별 찍기 (좌표 변환 필요)
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'
        # 왜 max_y - y?
        # 일반적으로 (0,0)을 왼쪽 아래로 두지만, 문자열 출력에서는 위쪽부터 출력되기 때문에 y좌표를 반대로 변환
        # 왜 x - min_x?
        # min_x가 음수일 수도 있기 때문에, 가장 작은 x좌표를 0 기준으로 이동

    
    return [''.join(row) for row in grid] # 이중리스트 grid