def solution(s):
    answer = True
    
    s = s.lower()
    
    pCnt = 0
    yCnt = 0
    
    for i in s:
        if i == 'p':
            pCnt += 1
        elif i == 'y':
            yCnt += 1
    
    if pCnt != yCnt: 
        return False
        
    # p의 개수
    # y의 개수
    
    # p == y : True
    # p != y : False
    # p and y not in s : True
    
    

    return True