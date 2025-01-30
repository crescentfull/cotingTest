from collections import deque

def solution(progresses, speeds):
    answer = []  # 각 배포마다 기능 개수를 저장할 리스트
    queue = deque()  # 남은 작업 일수를 저장할 큐

    # 각 기능이 완료되는 데 필요한 일수 계산
    for p, s in zip(progresses, speeds):
        days = -((p - 100) // s)  # 남은 작업 %를 속도로 나누어 필요한 일수 계산
        queue.append(days)

    while queue:
        count = 1  # 현재 배포될 기능 개수
        first = queue.popleft()  # 첫 번째 기능의 배포 날짜

        # 큐에 남아 있는 기능들과 비교하여 함께 배포할 기능 개수 확인
        while queue and queue[0] <= first:
            queue.popleft()
            count += 1
        
        answer.append(count)  # 배포된 기능 개수 추가

    return answer