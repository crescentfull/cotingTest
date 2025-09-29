from functools import reduce

def multi(x,y):
    return x*y

def solution(num_list):
    answer = 0
    if reduce(multi, num_list) < sum(num_list)**2:
        return  1
    return answer