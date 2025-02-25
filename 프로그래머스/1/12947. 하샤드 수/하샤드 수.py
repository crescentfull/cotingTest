def solution(x):
    # x의 자릿수 합 계산
    digit_sum = sum(int(digit) for digit in str(x))  # 각 자릿수를 정수로 변환 후 합산
    
    # 하샤드 수 판별
    answer = x % digit_sum == 0  # 자릿수 합으로 x가 나누어 떨어지면 True, 아니면 False
    return answer