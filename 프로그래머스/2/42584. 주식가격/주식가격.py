def solution(prices):
    # 결과를 저장할 리스트를 prices와 같은 길이로 0으로 초기화
    answer = [0] * len(prices)
    stack = []  # 인덱스를 저장하는 스택
    
    # 각 시간대의 가격을 순회
    for i in range(len(prices)):
        # 스택이 비어있지 않고, 현재 가격이 스택에 저장된 이전 인덱스의 가격보다 낮으면
        while stack and prices[i] < prices[stack[-1]]:
            prev = stack.pop()  # 이전 인덱스를 꺼냄
            answer[prev] = i - prev  # 가격이 떨어진 시점을 계산
        
        # 현재 인덱스를 스택에 추가
        stack.append(i)
    
    # 끝까지 남아 있는 스택 처리
    while stack:
        prev = stack.pop()
        answer[prev] = len(prices) - 1 - prev  # 끝까지 가격이 떨어지지 않음
    
    return answer
