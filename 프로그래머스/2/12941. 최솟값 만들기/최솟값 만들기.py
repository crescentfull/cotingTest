def solution(A, B):
    # A 오름차순 정렬
    A.sort()
    # B 내림차순 정렬
    B.sort(reverse=True)
    
    answer = 0
    # 각 인덱스끼리 곱하여 누적합
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer