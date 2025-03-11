from itertools import permutations

def solution(k, dungeons):
    answer = -1
    max_dungeons = 0  # 탐험 가능한 최대 던전 개수 저장

    for perm in permutations(dungeons):  # 던전 순서의 모든 경우의 수 확인
        fatigue = k  # 현재 피로도
        count = 0  # 탐험한 던전 개수

        for min_fatigue, consume_fatigue in perm:
            if fatigue >= min_fatigue:  # 탐험 가능하면
                fatigue -= consume_fatigue  # 피로도 차감
                count += 1  # 탐험 던전 개수 증가
            else:
                break  # 탐험 불가능하면 종료
        
        max_dungeons = max(max_dungeons, count)  # 최대 던전 개수 업데이트

    answer = max_dungeons
    return answer
