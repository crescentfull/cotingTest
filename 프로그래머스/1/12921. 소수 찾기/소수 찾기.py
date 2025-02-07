def solution(n):
    answer = 0
    if n < 2:
        return 0  # 2 미만의 수에는 소수가 없음

    sieve = [True] * (n + 1)  # 초기 배열을 True로 설정 (소수 후보)
    sieve[0], sieve[1] = False, False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):  # 2부터 √n까지 반복
        if sieve[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수를 모두 제거
                sieve[j] = False

    answer = sum(sieve)  # True(소수)의 개수를 answer 변수에 저장
    return answer
