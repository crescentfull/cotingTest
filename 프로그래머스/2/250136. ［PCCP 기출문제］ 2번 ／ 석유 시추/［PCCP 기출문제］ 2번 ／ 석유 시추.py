def solution(land):
    n = len(land)
    m = len(land[0])

    # 방향 설정: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 방문 여부를 기록하기 위한 배열
    visited = [[False] * m for _ in range(n)]

    # 석유 덩어리 크기를 계산하는 DFS 함수
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        cluster = [(x, y)]
        size = 1  # 석유 덩어리의 크기
        
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    cluster.append((nx, ny))
                    size += 1
        
        return size, cluster

    # 열별로 어떤 덩어리가 지나가는지 기록하기 위한 리스트
    column_oil_contribution = [set() for _ in range(m)]
    oil_clusters = []  # 덩어리 크기 저장

    # 석유 덩어리를 찾고 그 크기와 좌표들을 기록
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size, cluster = dfs(i, j)
                oil_clusters.append(size)
                
                # 각 열에 해당 덩어리가 지나가는지를 기록
                for (x, y) in cluster:
                    column_oil_contribution[y].add(len(oil_clusters) - 1)  # 덩어리 인덱스 기록

    # 각 열에 대해 석유량 계산
    max_oil = 0
    for col in range(m):
        total_oil = sum(oil_clusters[idx] for idx in column_oil_contribution[col])
        max_oil = max(max_oil, total_oil)

    return max_oil
