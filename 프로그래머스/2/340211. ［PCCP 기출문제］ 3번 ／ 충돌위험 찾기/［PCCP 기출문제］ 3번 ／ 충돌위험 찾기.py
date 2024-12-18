def solution(points, routes):
    # points[i]는 i번째 포인트(1-based index)의 (r, c)
    # 포인트 인덱스 접근 편의를 위해 딕셔너리화
    point_dict = {i+1: (p[0], p[1]) for i, p in enumerate(points)}

    # 각 로봇의 이동 경로(시간별 위치)를 담는 리스트
    robots_paths = []

    # 각 로봇에 대해 이동 경로 계산
    for route in routes:
        # route: [p1, p2, ..., pm]
        # 로봇 시작 시점: t=0, p1 위치
        robot_positions = []
        cur_r, cur_c = point_dict[route[0]]
        robot_positions.append((cur_r, cur_c))  # t=0 위치
        
        # 각 포인트 쌍에 대해 이동 경로 추가
        for i in range(len(route)-1):
            start_p = route[i]
            end_p = route[i+1]
            start_r, start_c = point_dict[start_p]
            end_r, end_c = point_dict[end_p]

            # 현재 위치는 이미 start_p 끝에 있으므로 여기서부터 end_p까지 이동
            # 지금 cur_r, cur_c는 start_p 위치.
            # end_r, end_c로 이동
            while (cur_r, cur_c) != (end_r, end_c):
                # r좌표부터 맞추기
                if cur_r < end_r:
                    cur_r += 1
                elif cur_r > end_r:
                    cur_r -= 1
                else:
                    # r이 맞춰졌다면 c좌표 이동
                    if cur_c < end_c:
                        cur_c += 1
                    elif cur_c > end_c:
                        cur_c -= 1
                robot_positions.append((cur_r, cur_c))
        
        # 로봇 경로 완성
        robots_paths.append(robot_positions)

    # 이제 모든 로봇의 경로가 robots_paths에 있음
    # 모든 로봇이 끝날 때까지(가장 긴 경로 길이) 시뮬레이션
    max_time = max(len(path) for path in robots_paths)

    # 초마다 위험 상황 계산
    total_danger = 0
    for t in range(max_time):
        # t초에 각 로봇 위치 count
        position_count = {}
        for path in robots_paths:
            if t < len(path):  # 아직 로봇이 운송 중이라면
                pos = path[t]
                position_count[pos] = position_count.get(pos, 0) + 1
        
        # 위험 상황: 로봇이 2대 이상 있는 좌표의 수
        for pos, count in position_count.items():
            if count >= 2:
                total_danger += 1

    return total_danger
