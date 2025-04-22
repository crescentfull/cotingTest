def solution(s):
    answer = True
    n = len(s)
    
    if n in (4, 6) and s.isdigit():
        return True
    else:
        return False
    
    return answer

