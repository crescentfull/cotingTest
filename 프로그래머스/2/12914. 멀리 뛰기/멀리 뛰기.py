def solution(n):
    answer = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    MOD = 1234567  # 나눌 값

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD  # 점화식 적용 및 나머지 연산
    
    answer = dp[n]
    return answer