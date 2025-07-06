def solution(my_string):
    answer = ''
    new_string = my_string.lower()
    answer = ''.join(sorted(new_string))
    return answer