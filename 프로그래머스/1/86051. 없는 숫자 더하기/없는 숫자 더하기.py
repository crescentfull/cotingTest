def solution(numbers):
    answer = -1
    check_numbers = [0,1,2,3,4,5,6,7,8,9]
    number = 0
    
    for check_number in check_numbers:
        if check_number not in numbers:
            number += check_number
            
    answer = number
    return answer