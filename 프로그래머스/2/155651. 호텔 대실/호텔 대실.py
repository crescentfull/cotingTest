def solution(book_time):
    # 시간을 분 단위로 변환하는 함수
    def time_to_minutes(time):
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes

    events = []
    
    # 각 예약을 시작 시간과 종료 시간(청소 포함)으로 변환
    for start, end in book_time:
        start_min = time_to_minutes(start)
        end_min = time_to_minutes(end) + 10  # 청소 시간 추가
        events.append((start_min, 'start'))
        events.append((end_min, 'end'))
    
    # 이벤트를 시간 순으로 정렬 (동일 시간일 경우, 종료 이벤트를 먼저 처리)
    events.sort(key=lambda x: (x[0], x[1] == 'start'))
    
    max_rooms = 0
    current_rooms = 0
    
    # 스위핑 처리
    for time, event in events:
        if event == 'start':
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
        elif event == 'end':
            current_rooms -= 1
    
    return max_rooms
