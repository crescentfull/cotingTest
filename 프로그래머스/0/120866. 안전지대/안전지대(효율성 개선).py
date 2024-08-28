'''
불필요 중복 탐색 제거 : 이미 위험 지역으로 표시된 칸을 다시 탐색하지 않도록 최적화
위험 지역 따로 표시할 배열 사용 : 'set' 대신 동일한 크기의 2차원 배열을 만들어 위험 지역을 표시

danger_map 배열 사용:
안전한 지역 계산:
danger_map과 board 배열을 동시에 확인하여 안전한 지역의 칸 수를 계산
지뢰가 없고(board[i][j] == 0), 위험 지역이 아닌(danger_map[i][j] == 0) 칸의 수를 answer에 저장
'''
def solution(board):
    n = len(board)  # board의 크기
    danger_map = [[0] * n for _ in range(n)]  # 위험 지역을 표시할 배열
    answer = 0  # 안전한 지역의 칸 수를 저장할 변수

    # 모든 지뢰의 위치를 탐색
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있는 경우
                # 지뢰의 위치와 그 주변 8방향을 위험 지역으로 표시
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        nx, ny = i + x, j + y
                        if 0 <= nx < n and 0 <= ny < n:  # 유효한 인덱스인지 확인
                            danger_map[nx][ny] = 1  # 위험 지역으로 표시

    # 안전한 지역의 칸 수 계산
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and danger_map[i][j] == 0:  # 지뢰가 없고 위험 지역이 아닌 경우
                answer += 1  # 안전한 칸 수를 증가

    return answer
