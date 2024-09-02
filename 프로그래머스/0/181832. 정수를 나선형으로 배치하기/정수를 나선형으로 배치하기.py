def solution(n):
    # n x n 크기의 이차원 배열을 0으로 초기화
    matrix = [[0] * n for _ in range(n)]
    
    # 방향 설정: 오른쪽(→), 아래(↓), 왼쪽(←), 위(↑) 순서
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # 현재 방향을 가리키는 인덱스 (초기: 오른쪽)
    
    # 초기 위치 설정
    x, y = 0, 0  # 시작 위치: [0, 0]
    num = 1  # 배열에 채울 첫 번째 숫자

    # 1부터 n^2까지 숫자를 배열에 채우기
    while num <= n * n:
        matrix[x][y] = num  # 현재 위치에 숫자를 채움
        num += 1  # 다음에 채울 숫자 증가
        
        # 다음 위치 계산
        dx, dy = directions[direction_index]  # 현재 방향에 따른 이동 벡터
        nx, ny = x + dx, y + dy  # 다음 위치 계산
        
        # 다음 위치가 배열의 경계를 벗어나거나 이미 채워진 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            # 시계방향으로 방향 전환
            direction_index = (direction_index + 1) % 4  # 방향 인덱스를 0, 1, 2, 3 순환
            dx, dy = directions[direction_index]  # 새로운 방향에 따른 이동 벡터
            nx, ny = x + dx, y + dy  # 전환된 방향으로 다음 위치 계산
        
        # 위치 갱신
        x, y = nx, ny
    
    return matrix  # 최종적으로 완성된 나선형 배열 반환
