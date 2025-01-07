def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # 최대 H-Index 계산
    h_index = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:  # 현재 논문이 (i+1)번 이상 인용되었는지 확인
            h_index = i + 1       # H-Index 갱신
        else:
            break                 # 조건을 만족하지 않으면 루프 종료
    
    return h_index
