def solution(a, b, n):
    total_cola = 0  # 상빈이가 받을 총 콜라 병 수

    while n >= a:
        new_cola = (n // a) * b  # 빈 병을 a개 단위로 교환하여 받을 수 있는 콜라 수
        total_cola += new_cola  # 받은 콜라의 수를 누적
        n = n % a + new_cola  # 마신 콜라의 빈 병을 더해 새로운 빈 병의 수 갱신

    return total_cola
