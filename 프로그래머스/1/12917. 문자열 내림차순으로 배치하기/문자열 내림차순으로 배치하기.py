def solution(s):
    answer = ''
    new = list(s)
    new.sort(reverse=True)
    answer = ''.join(new)
    
    return answer