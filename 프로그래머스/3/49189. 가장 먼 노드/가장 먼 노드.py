from collections import deque

def solution(n, vertex):
    # 그래프 인접 리스트 초기화
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)  # 양방향 그래프

    # BFS를 위한 큐 및 거리 정보 저장 리스트 초기화
    queue = deque([1])  # 1번 노드에서 시작
    distances = {i: -1 for i in range(1, n + 1)}  # 방문하지 않은 노드는 -1
    distances[1] = 0  # 시작 노드는 거리 0

    # BFS 수행
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:  # 현재 노드와 연결된 모든 노드 탐색
            if distances[neighbor] == -1:  # 방문하지 않은 경우만 처리
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # 가장 먼 거리 찾기
    max_distance = max(distances.values())  # 최장 거리
    return list(distances.values()).count(max_distance)  # 최장 거리 노드 개수 반환

# 테스트 실행
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))  # 3
