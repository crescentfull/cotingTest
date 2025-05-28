def solution(a, b):
    answer = 0
    cal1 = int(str(a)+str(b))
    cal2 = int(str(b)+str(a))
    
    answer = cal2 if cal2 > cal1 else cal1
    
    return answer