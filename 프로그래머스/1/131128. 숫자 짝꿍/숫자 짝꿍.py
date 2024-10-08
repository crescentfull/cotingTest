from collections import Counter

def solution(X, Y):
    # 각 숫자의 등장 횟수를 세기 위해 Counter를 사용
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    # 공통으로 나타나는 숫자 중 최소 등장 횟수만큼 가져오기
    common_digits = []
    
    for digit in range(10):
        str_digit = str(digit)
        if str_digit in count_X and str_digit in count_Y:
            # 각 숫자가 X와 Y에서 공통으로 나타나는 최소 개수만큼 추가
            common_digits += [str_digit] * min(count_X[str_digit], count_Y[str_digit])
    
    # 공통 숫자가 없으면 -1 반환
    if not common_digits:
        return "-1"
    
    # 공통 숫자를 내림차순으로 정렬하여 가장 큰 수 만들기
    common_digits.sort(reverse=True)
    
    # 만약 결과가 '0'으로만 이루어졌다면, '0' 반환
    if common_digits[0] == "0":
        return "0"
    
    # 결과 문자열 반환
    return ''.join(common_digits)
