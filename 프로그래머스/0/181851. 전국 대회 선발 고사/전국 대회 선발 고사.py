def solution(rank, attendance):
    answer = 0
    # 참석 가능한 학생들의 (등수, 학생 번호) 리스트 생성
    candidates = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    
    # 등수를 기준으로 오름차순 정렬
    candidates.sort()
    
    # 상위 3명의 학생 번호 추출
    a, b, c = candidates[0][1], candidates[1][1], candidates[2][1]
    
    # 결과값 계산
    answer = (10000 * a) + (100 * b) + c
    
    return answer