def solution(park, routes):
    # 공원의 크기와 방향별 이동 정의
    H, W = len(park), len(park[0])
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    # 시작 위치 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x, y = i, j  # 시작 지점 저장
                break
    
    # 명령 처리
    for route in routes:
        op, n = route.split()
        n = int(n)
        dx, dy = directions[op]  # 방향에 따른 이동 좌표
        
        # 이동 가능성 확인
        nx, ny = x, y
        valid = True
        for _ in range(n):
            nx += dx
            ny += dy
            
            # 공원 범위를 벗어나거나 장애물에 부딪히는 경우
            if nx < 0 or nx >= H or ny < 0 or ny >= W or park[nx][ny] == 'X':
                valid = False
                break
        
        # 이동 가능하면 위치 갱신
        if valid:
            x, y = nx, ny
    
    # 최종 위치 반환
    return [x, y]
