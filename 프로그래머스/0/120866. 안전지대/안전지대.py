def solution(board):
    answer = 0
    n = len(board)  # board의 크기
    danger_zone = set()  # 위험 지역을 저장할 집합

    # 모든 지뢰의 위치를 탐색
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있는 경우
                # 지뢰 주변 8방향을 탐색하여 위험 지역으로 설정
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        nx, ny = i + x, j + y
                        if 0 <= nx < n and 0 <= ny < n:  # 유효한 인덱스인지 확인
                            danger_zone.add((nx, ny))

    # 전체 칸 수에서 위험 지역을 제외한 안전한 지역의 칸 수 계산
    answer = n * n - len(danger_zone)
    
    return answer  # answer 변수로 반환
