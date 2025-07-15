def multiply(nums):
    res = 1
    for i in nums:
        if i == 0:
            return 0
        res *= i
    return res
        
    
def solution(num_list):
    answer = 0
    if len(num_list) > 10:
        answer = sum(num_list)        
    else:
        answer = multiply(num_list)
    return answer