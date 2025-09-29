from math import prod

def solution(num_list):
    answer = 0
    if prod(num_list) < sum(num_list)**2:
        return 1
    return answer


# 1.첫번째
# from functools import reduce

# def multi(x,y):
#     return x*y

# def solution(num_list):
#     answer = 0
    
#     if reduce(multi, num_list) < sum(num_list)**2:
#         return 1
    
#     return answer
