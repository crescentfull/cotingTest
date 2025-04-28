def solution(n, t):
    answer = 0
    for i in range(t):
        answer = n*2
        n = answer
    return answer