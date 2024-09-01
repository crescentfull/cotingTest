def solution(lines):
    # 좌표 범위가 -100 ~ 100이므로 이를 0 ~ 200으로 변환하여 사용할 배열을 준비
    line_map = [0] * 201  # 각 좌표에서 겹치는 선분 수를 저장할 배열

    # 각 선분의 시작과 끝을 순회하며 겹치는 부분을 기록
    for start, end in lines:
        for i in range(start + 100, end + 100):  # 시작과 끝점을 변환하여 0 ~ 200의 범위로 사용
            line_map[i] += 1

    # 두 개 이상의 선분이 겹친 구간의 길이 계산
    answer = sum(1 for count in line_map if count > 1)
    
    return answer