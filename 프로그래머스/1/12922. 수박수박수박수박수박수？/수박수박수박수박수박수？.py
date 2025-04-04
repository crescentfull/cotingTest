def solution(n):
    answer = ''
    str = "수박"
    
    if n > 1:
        if n % 2 == 0:
            answer += str*(n//2)
        if n % 2 != 0 :
            answer += (str*(n//2) + "수")
    else:
        answer += "수"
            
    return answer