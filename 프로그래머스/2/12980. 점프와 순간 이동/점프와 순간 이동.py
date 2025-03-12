def solution(n):
    answer = 0  # 사용한 건전지 양
    
    while n > 0:
        if n % 2 == 0:  
            n //= 2  # 순간이동
        else:
            answer += 1  # 점프
            n -= 1  # 점프 후 순간이동 가능하도록 변경
    
    return answer
# def solution(n):
#     return bin(n).count('1')