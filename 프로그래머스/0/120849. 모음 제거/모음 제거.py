def solution(my_string):
    answer = ''
    moeum = "aeiou"
    for i in my_string:
        if i not in moeum:
            answer += i
    return answer