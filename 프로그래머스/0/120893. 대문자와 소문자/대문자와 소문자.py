def solution(my_string):
    answer = ''
    for i in my_string:
        if i == str.upper(i):
            i = str.lower(i)
            answer += i
        else:
            i = str.upper(i)
            answer += i
    return answer