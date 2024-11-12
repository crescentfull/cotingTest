def solution(participant, completion):
    # 참가자와 완주자 명단을 정렬합니다.
    participant.sort()
    completion.sort()
    
    # 정렬된 명단을 순서대로 비교하여 다른 지점을 찾습니다.
    for p, c in zip(participant, completion):
        if p != c:
            return p  # 완주하지 못한 선수 발견 시 반환합니다.
    
    # 마지막에 남은 선수가 완주하지 못한 선수입니다.
    return participant[-1]
