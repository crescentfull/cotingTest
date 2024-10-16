import math

def solution(n, m):
    gcd_value = math.gcd(n, m)  # 최대공약수 구하기
    lcm_value = (n * m) // gcd_value  # 최소공배수 구하기
    return [gcd_value, lcm_value]