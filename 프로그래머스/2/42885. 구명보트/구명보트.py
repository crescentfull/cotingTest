def solution(people, limit):
    people.sort()  # 몸무게를 오름차순으로 정렬
    left, right = 0, len(people) - 1  # 투 포인터 초기화
    answer = 0  # 필요한 구명보트 개수
    
    while left <= right:
        if people[left] + people[right] <= limit:  # 두 사람이 함께 탈 수 있으면
            left += 1  # 가벼운 사람도 태움
        right -= 1  # 무거운 사람 태우기
        answer += 1  # 보트 개수 증가
    
    return answer