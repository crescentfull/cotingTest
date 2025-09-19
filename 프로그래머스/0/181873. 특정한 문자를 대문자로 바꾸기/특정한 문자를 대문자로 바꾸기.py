def solution(my_string, alp):
    answer = ''
    if alp not in my_string:
        return my_string
    else:
        for i in my_string:
            if i == alp:
                answer = my_string.replace(i,i.upper())
            
    return answer