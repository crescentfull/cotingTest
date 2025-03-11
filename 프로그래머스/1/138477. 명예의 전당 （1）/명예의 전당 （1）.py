import heapq

def solution(k, score):
    hall_of_fame = []  # 명예의 전당 (최소 힙)
    answer = []

    for s in score:
        heapq.heappush(hall_of_fame, s)  # 점수를 힙에 추가
        if len(hall_of_fame) > k:  # k개를 초과하면 
            heapq.heappop(hall_of_fame) # 최하위 점수 제거
        answer.append(hall_of_fame[0])  # 현재 명예의 전당 최하위 점수 저장

    return answer
