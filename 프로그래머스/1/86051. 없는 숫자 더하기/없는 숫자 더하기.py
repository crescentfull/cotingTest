def solution(numbers):
    answer = 0
    
    for number in range(0,10):
        if number not in numbers:
            answer += number
            
    return answer