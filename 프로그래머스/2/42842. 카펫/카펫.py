def solution(brown, yellow):
    total = brown + yellow  # 전체 격자 개수

    for h in range(1, int(total ** 0.5) + 1):  # h는 total의 약수 중 하나
        if total % h == 0:  # total을 나눌 수 있어야 함
            w = total // h  # 가로 길이 계산
            if w >= h and (2 * w + 2 * h - 4) == brown:  # 갈색 타일 조건 확인
                answer = [w, h]
                return answer