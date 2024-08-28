import math
def solution(numer1, denom1, numer2, denom2):
    # 두 분모의 최소공배수를 구함 (LCM = (denom1 * denom2) / GCD(denom1, denom2))
    lcm = (denom1 * denom2) // math.gcd(denom1, denom2)
    
    # 공통 분모(lcm)를 기준으로 새로운 분자를 계산
    # 첫 번째 분수의 새로운 분자 = numer1 * (lcm // denom1)
    # 두 번째 분수의 새로운 분자 = numer2 * (lcm // denom2)
    # 두 분수를 더한 새로운 분자 = 두 분자의 합
    new_numer = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)
    new_denom = lcm  # 공통 분모로 설정

    # 새로운 분자와 분모의 최대공약수(GCD)를 구함
    gcd = math.gcd(new_numer, new_denom)
    
    # 최대공약수로 나누어 기약 분수로 만듦
    result_numer = new_numer // gcd  # 기약 분수의 분자
    result_denom = new_denom // gcd  # 기약 분수의 분모

    # 결과를 [분자, 분모] 형태의 배열로 answer에 저장
    answer = [result_numer, result_denom]
    
    # answer를 반환
    return answer