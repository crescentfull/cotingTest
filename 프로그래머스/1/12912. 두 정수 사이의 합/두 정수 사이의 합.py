def solution(a, b):
    answer = 0
    if a > b:
        n = b
        b = a
        a = n
    for i in range(a,b+1):
         answer += i
    return answer