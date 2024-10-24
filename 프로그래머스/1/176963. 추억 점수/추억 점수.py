def solution(name, yearning, photo):
    answer = []
    
    # 이름과 그리움 점수를 매핑하는 딕셔너리 생성
    # 각 사람의 이름 = key, 그리움 점수 = value
    score_dict = {n: y for n, y in zip(name, yearning)}
    
    # photo 배열에 있는 각 사진에 대해 반복문을 실행
    for p in photo:
        # 각 사진에서 인물들의 추억 점수를 합산할 변수 total_score 초기화
        total_score = 0
        
        # 사진에 포함된 인물들을 순회
        for person in p:
            # 그리움 점수를 알고 있는 인물이라면 그 점수를 더함
            if person in score_dict:
                total_score += score_dict[person]
        
        # 해당 사진의 추억 점수를 result 리스트에 추가
        answer.append(total_score)
    
    # 모든 사진의 추억 점수를 계산한 후 결과 리스트를 반환
    return answer
