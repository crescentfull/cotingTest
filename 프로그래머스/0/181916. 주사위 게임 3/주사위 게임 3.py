def solution(a, b, c, d):
    answer = 0

    # 주사위 숫자의 빈도를 저장할 배열 (인덱스 0은 사용하지 않음)
    count = [0] * 7
    
    # 각 주사위 숫자의 빈도 계산
    for num in [a, b, c, d]:
        count[num] += 1

    # 등장 빈도에 따라 점수를 계산
    freq = sorted([(count[i], i) for i in range(1, 7) if count[i] > 0], reverse=True)

    # 조건에 따른 점수 계산
    if freq[0][0] == 4:
        # 모든 숫자가 같음: 1111 * p
        p = freq[0][1]
        answer = 1111 * p
    elif freq[0][0] == 3:
        # 세 주사위가 같은 경우: (10 * p + q) ** 2
        p = freq[0][1]
        q = freq[1][1]
        answer = (10 * p + q) ** 2
    elif freq[0][0] == 2 and freq[1][0] == 2:
        # 두 개씩 같은 경우: (p + q) * abs(p - q)
        p = freq[0][1]
        q = freq[1][1]
        answer = (p + q) * abs(p - q)
    elif freq[0][0] == 2:
        # 두 주사위만 같은 경우: q * r
        p = freq[0][1]
        q, r = freq[1][1], freq[2][1]
        answer = q * r
    else:
        # 모두 다른 경우: 최소값 반환
        answer = min(a, b, c, d)
    
    return answer