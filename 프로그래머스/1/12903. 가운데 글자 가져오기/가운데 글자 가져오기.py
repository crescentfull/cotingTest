def solution(s):
    answer = ''
    method = len(s) % 2
    sol = len(s) // 2
    if method == 0:
        answer = s[sol-1]+s[sol]
    else:
        answer = s[sol]
    return answer