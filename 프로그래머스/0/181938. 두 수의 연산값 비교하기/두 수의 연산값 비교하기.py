def solution(a, b):
    answer = 0
    new_sum = int(str(a)+str(b))
    second_sum = 2*a*b
    
    answer = new_sum if new_sum > second_sum else second_sum
    
    
    return answer