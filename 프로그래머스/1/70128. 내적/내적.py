def solution(a, b):
    answer = 0
    answer = sum( a[i]*b[i] for i in range(len(a)))
    return answer