def solution(n):
    answer = 0
    
    # k(길이)를 1부터 증가시키며 가능한 경우 탐색
    k = 1
    while k * (k - 1) // 2 < n:  # 등차수열의 합 조건
        # 등차수열의 합 공식 변형: (n - k(k-1)/2) % k == 0 이면 k 길이의 연속합 가능
        if (n - k * (k - 1) // 2) % k == 0:
            answer += 1
        k += 1
    
    return answer
