def solution(d, budget):
    # 1. 부서별 신청 금액을 오름차순으로 정렬
    d.sort()
    
    # 2. 지원 가능한 부서의 수를 저장할 변수
    count = 0
    
    # 3. 부서 신청 금액을 하나씩 예산에서 빼면서 계산
    for amount in d:
        if budget >= amount:
            budget -= amount  # 예산에서 해당 금액을 빼줌
            count += 1        # 지원 가능한 부서 수 증가
        else:
            break  # 예산이 부족하면 반복을 종료
    
    # 4. 최대 지원 가능한 부서 수를 반환
    return count