# import math

# def solution(n):
#     # n의 제곱근을 구하기
#     sqrt_n = math.sqrt(n)
    
#     # 제곱근이 정수인지 확인
#     if sqrt_n.is_integer():
#         # 정수라면, (sqrt_n + 1)의 제곱을 반환
#         return int((sqrt_n + 1) ** 2)
#     else:
#         # 정수가 아니라면 -1을 반환
#         return -1

def solution(n):
    # 탐색할 범위의 시작과 끝을 설정
    # 여기서는 1부터 n까지의 값 중에서 n의 제곱근에 해당하는 정수를 찾는다
    low, high = 1, n
    
    # low가 high보다 작거나 같은 동안 반복하여 탐색
    while low <= high:
        # 중간값(mid)을 구한다. 이 값은 현재 탐색 범위의 중앙
        mid = (low + high) // 2
        # 중간값의 제곱을 계산
        square = mid * mid
        
        # 만약 중간값의 제곱이 n과 같다면, n은 완전제곱수
        # 따라서 (mid + 1)의 제곱이 정답
        if square == n:
            return (mid + 1) * (mid + 1)
        # 만약 중간값의 제곱이 n보다 작다면,
        # n은 더 큰 값의 제곱일 가능성이 있으므로 탐색 범위를 중간값의 오른쪽(큰 수 쪽)으로 좁힌다
        elif square < n:
            low = mid + 1
        # 만약 중간값의 제곱이 n보다 크다면,
        # n은 더 작은 값의 제곱일 가능성이 있으므로 탐색 범위를 중간값의 왼쪽(작은 수 쪽)으로 좁힌다
        else:
            high = mid - 1
    
    # 만약 while문을 빠져나온다면, n은 어떤 정수의 제곱이 아니므로 -1을 반환
    return -1