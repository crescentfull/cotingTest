def solution(s):
    # 문자열을 공백 기준으로 분리하여 정수 리스트로 변환
    numbers = list(map(int, s.split()))
    
    # 최소값과 최대값 계산
    min_value = min(numbers)
    max_value = max(numbers)
    
    # 최소값과 최대값을 문자열로 결합하여 반환
    return f"{min_value} {max_value}"