def solution(n, lost, reserve):
    # 여벌 체육복을 가져왔으나 도난당한 학생을 제외
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)

    # 여벌 체육복을 빌려줌
    for r in sorted(reserve_only):
        if r - 1 in lost_only:
            lost_only.remove(r - 1)
        elif r + 1 in lost_only:
            lost_only.remove(r + 1)
    
    # 수업을 들을 수 있는 학생의 수는 전체 학생 수 - 체육복을 여전히 잃어버린 학생 수
    return n - len(lost_only)