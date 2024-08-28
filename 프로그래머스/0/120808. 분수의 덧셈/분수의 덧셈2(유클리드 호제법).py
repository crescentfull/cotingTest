def solution(numer1, denom1, numer2, denom2):
    answer = [ ]
    # 최대공약수를 계산하는 함수 (유클리드 호제법)
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # 최소공배수를 계산하는 함수
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    
    # 두 분모의 최소공배수를 구함
    common_denom = lcm(denom1, denom2)

    # 공통 분모를 기준으로 새로운 분자를 계산
    new_numer = numer1 * (common_denom // denom1) + numer2 * (common_denom // denom2)
    new_denom = common_denom

    # 새로운 분자와 분모의 최대공약수를 구함
    common_gcd = gcd(new_numer, new_denom)
    
    # 최대공약수로 나누어 기약 분수로 만듦
    result_numer = new_numer // common_gcd
    result_denom = new_denom // common_gcd

    # 결과를 [분자, 분모] 형태의 배열로 answer에 저장
    answer = [result_numer, result_denom]
    
    # answer를 반환
    return answer
