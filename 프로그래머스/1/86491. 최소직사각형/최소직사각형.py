def solution(sizes):
    # 명함의 크기를 회전시켜 큰 값을 가로, 작은 값을 세로로 정렬
    max_width = 0
    max_height = 0
    
    for w, h in sizes:
        # 가로, 세로 중 큰 값을 가로로, 작은 값을 세로로 정렬
        if w < h:
            w, h = h, w
        # 최대 가로, 최대 세로 찾기
        max_width = max(max_width, w)
        max_height = max(max_height, h)
    
    # 지갑의 크기 계산
    return max_width * max_height