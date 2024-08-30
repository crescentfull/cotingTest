from collections import Counter

def solution(a, b, c, d):
    # 주사위 숫자들을 리스트로 만들고, 각 숫자의 빈도를 센다
    dice = [a, b, c, d]
    count = Counter(dice)
    
    # 빈도 수가 높은 순서대로 정렬 (key: 빈도, value: 숫자)
    counts = sorted(count.items(), key=lambda x: -x[1])
    
    # 조건에 따른 점수 계산
    if counts[0][1] == 4:
        # 모든 숫자가 같음: 1111 * p
        p = counts[0][0]
        answer = 1111 * p
    elif counts[0][1] == 3:
        # 세 주사위가 같은 경우: (10 * p + q) ** 2
        p = counts[0][0]
        q = counts[1][0]
        answer = (10 * p + q) ** 2
    elif counts[0][1] == 2 and counts[1][1] == 2:
        # 두 개씩 같은 경우: (p + q) * abs(p - q)
        p = counts[0][0]
        q = counts[1][0]
        answer = (p + q) * abs(p - q)
    elif counts[0][1] == 2:
        # 두 주사위만 같은 경우: q * r
        p = counts[0][0]
        q, r = counts[1][0], counts[2][0]
        answer = q * r
    else:
        # 모두 다른 경우: 최소값 반환
        answer = min(dice)
    
    return answer

# 입출력 예시 테스트
print(solution(2, 2, 2, 2))  # 2222
print(solution(4, 1, 4, 4))  # 1681
print(solution(6, 3, 3, 6))  # 27
print(solution(2, 5, 2, 6))  # 30
print(solution(6, 4, 2, 5))  # 2
