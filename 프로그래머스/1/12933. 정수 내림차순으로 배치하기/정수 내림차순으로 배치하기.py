def solution(n):
    answer = 0
    res = list(str(n))
    res.sort(reverse = True)
    answer = ''.join(res)
    #print(int(answer)) 
    return int(answer)