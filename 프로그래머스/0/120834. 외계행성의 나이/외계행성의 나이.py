def solution(age):
    answer = ''
    new_age = 'abcdefghij'
    num = '0123456789'
    
    convert = {key: value for key, value in zip(num, new_age)}

    for i in str(age):
        answer += convert[i]
        
    return answer