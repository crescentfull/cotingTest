def solution(n):
    answer = 0
    
    # n을 x로 나누면 나머지가 1이 되야한다.
    for x in range(1, n+1):
        if n % x == 1:
            return x
            break
    
    # n을 x로 나누었을때 가장작은 숫자가 반횐되어야 한다.
    
    return answer