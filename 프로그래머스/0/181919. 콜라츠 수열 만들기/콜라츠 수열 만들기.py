def solution(n):
    answer = []
    print(n)
    answer.append(n)
    while n!=1:
        if n % 2 == 0:
            n = n//2
        elif n % 2 != 0:
            n = 3*n+1
        answer.append(n)
    return answer