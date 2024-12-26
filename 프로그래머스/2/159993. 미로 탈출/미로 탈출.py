from collections import deque

def solution(maps):
    # 행, 열 크기
    n, m = len(maps), len(maps[0])
    
    # S, L, E 좌표 초기화
    S = L = E = None
    
    # S, L, E의 위치를 찾는다.
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
    
    # BFS 함수 정의: start에서 goal까지 가는 최단 거리
    def bfs(start, goal):
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        queue.append((*start, 0))  # (row, col, 이동 거리)
        visited[start[0]][start[1]] = True
        
        # 방향(상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, dist = queue.popleft()
            
            # 목표 지점 도달 시 거리 반환
            if (r, c) == goal:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 유효 범위 체크 & 방문 여부 & 벽이 아닌지 확인
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc] and maps[nr][nc] != 'X':
                        visited[nr][nc] = True
                        queue.append((nr, nc, dist + 1))
        
        # 도달 불가능하면 -1
        return -1
    
    # 1) S → L 최단거리
    dist_SL = bfs(S, L)
    if dist_SL == -1:
        return -1
    
    # 2) L → E 최단거리
    dist_LE = bfs(L, E)
    if dist_LE == -1:
        return -1
    
    # 두 구간의 최단거리 합
    return dist_SL + dist_LE
