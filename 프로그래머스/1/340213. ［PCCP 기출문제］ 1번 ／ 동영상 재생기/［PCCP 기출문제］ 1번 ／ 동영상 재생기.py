def solution(video_len, pos, op_start, op_end, commands):
    # 문자열 "mm:ss"를 총 초로 변환하는 헬퍼 함수
    def to_seconds(t):
        mm, ss = t.split(':')
        return int(mm) * 60 + int(ss)
    
    # 초를 "mm:ss" 문자열로 변환하는 헬퍼 함수
    def to_mmss(s):
        mm = s // 60
        ss = s % 60
        return f"{mm:02d}:{ss:02d}"
    
    # 주어진 시간들을 초 단위로 변환
    video_len_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    op_start_sec = to_seconds(op_start)
    op_end_sec = to_seconds(op_end)
    
    # 처음 시작 위치가 오프닝 구간 안에 있는지 체크
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    
    # 명령어 처리
    for cmd in commands:
        if cmd == "prev":
            # 10초 전으로 이동
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
        elif cmd == "next":
            # 10초 후로 이동
            pos_sec += 10
            if pos_sec > video_len_sec:
                pos_sec = video_len_sec
        
        # 오프닝 구간 체크
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
    
    # 최종 위치를 "mm:ss" 형태로 변환
    return to_mmss(pos_sec)
