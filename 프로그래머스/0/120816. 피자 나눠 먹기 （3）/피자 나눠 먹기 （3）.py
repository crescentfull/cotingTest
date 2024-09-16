def solution(slice, n):
    # 필요한 피자 판 수를 계산
    answer = (n + slice - 1) // slice
    return answer