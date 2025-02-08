def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)  # 점수를 내림차순 정렬
    
    # m개씩 묶을 수 있는 최대 개수만큼 반복
    for i in range(0, len(score) - m + 1, m):
        answer += score[i + m - 1] * m  # 가장 낮은 점수 × 상자 크기
    
    return answer