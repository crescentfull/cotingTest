def solution(n):
    # 첫 두 피보나치 수 초기화
    a, b = 0, 1
    
    # n번째 피보나치 수 계산
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1234567
    
    return b