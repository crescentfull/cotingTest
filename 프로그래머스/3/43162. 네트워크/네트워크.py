def solution(n, computers):
    # 방문 여부를 기록하는 리스트
    visited = [False] * n

    def dfs(node):
        # 현재 노드를 방문 처리
        visited[node] = True
        # 연결된 다른 노드를 탐색
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    # 네트워크 개수를 저장할 변수
    network_count = 0

    # 모든 컴퓨터를 순회하며 네트워크 탐색
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 컴퓨터라면
            dfs(i)          # DFS를 통해 해당 네트워크 탐색
            network_count += 1  # 새로운 네트워크 발견

    return network_count