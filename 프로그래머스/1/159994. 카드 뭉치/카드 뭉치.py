from collections import deque  # 큐(Queue) 자료구조 사용

def solution(cards1, cards2, goal):
    
    queue1 = deque(cards1)  # cards1을 큐로 변환
    queue2 = deque(cards2)  # cards2를 큐로 변환
    
    for word in goal:  # goal의 단어들을 순차적으로 확인
        if queue1 and queue1[0] == word:  # queue1의 첫 번째 원소가 목표 단어와 같다면
            queue1.popleft()  # queue1에서 제거
        elif queue2 and queue2[0] == word:  # queue2의 첫 번째 원소가 목표 단어와 같다면
            queue2.popleft()  # queue2에서 제거
        else:
            return "No"  # 두 큐의 첫 번째 원소가 모두 일치하지 않으면 만들 수 없음
    
    return "Yes"  # goal의 모든 단어를 순서대로 만들었다면 "Yes" 반환