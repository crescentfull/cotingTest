def solution(hp):
    answer = 0
    # 장군 = 5
    # 병정개미 = 3
    # 일개미 = 1
    ants = [5,3,1]
    cnt = 0
    for ant in ants:
        if hp % ant != 0 :
            cnt += hp//ant
            hp = hp%ant
        elif hp % ant == 0:
            cnt += hp//ant
            hp = hp%ant
    answer = cnt        
    return answer