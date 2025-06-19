def solution(my_string, num1, num2):
    answer = ''
    list_string = list(my_string)
    list_string[num1], list_string[num2] = list_string[num2], list_string[num1]
    
    return answer.join(list_string)