def solution(a, b):
    answer = 0
    if a > b:
        n = b
        b = a
        a = n
    return sum(range(a,b+1))