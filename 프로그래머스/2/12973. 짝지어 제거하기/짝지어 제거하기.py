def solution(s):
    stack = []
    
    for char in s:  # 문자열의 각 문자에 대해 순회
        if stack and stack[-1] == char:  # 스택의 마지막 문자와 현재 문자가 같으면
            stack.pop()  # 짝을 이루므로 제거 (pop)
        else:
            stack.append(char)  # 짝이 아니면 스택에 추가
    
    answer = 1 if not stack else 0  # 스택이 비었으면 1, 남아있으면 0을 저장
    return answer