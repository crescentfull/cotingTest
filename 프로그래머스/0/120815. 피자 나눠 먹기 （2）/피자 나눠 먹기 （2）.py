def gcd(a, b):
    # 최대공약수(GCD)를 유클리드 호제법으로 계산
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # 최소공배수(LCM) 계산: a * b // GCD(a, b)
    return a * b // gcd(a, b)

def solution(n):
    # 피자 조각 수와 사람 수 n의 최소공배수 계산
    pieces_needed = lcm(6, n)
    
    # 필요한 피자 판 수는 최소공배수를 6으로 나눈 값
    answer = pieces_needed // 6
    return answer
