def solution(emergency):
    # 딕셔너리로 값을 매겨주는데, 매개변수 값을 역순으로 정열하여 인덱스 값을 튜플로 뽑아주는 enumerate를 이용
    # (0,76),(1,24),(2,3)
    # 이렇게 반환 되니까 본래 key: value를 바꿔서 등록해줘야한다.(입력값과 같은 값의 우선순위를 뽑아줘야하니까)
    rank = {value: num+1 for num, value in enumerate(sorted(emergency, reverse=True))}
    
    return [rank[i] for i in emergency]
