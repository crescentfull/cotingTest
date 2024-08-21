def solution(quiz):
    answer = []

    for i in quiz:
        # expression(식) result(결과값) "=" 기준으로 나눠서 변수 저장
        expression, result = i.split(" = ") 
        # 계산 결과값을 정수로 변환
        result = int(result) 
        
        # 이제 식 변수에 저장된 string값을 정수와 연산자로 나눠서 변수 저장
        x, operator, y = expression.split()
        
        # 변수에 저장된 숫자 string 값을 int로 치환
        x = int(x) 
        y = int(y) 
        
        # 판별문으로 operator 연산자의 string에 대한 문자를 판별
        if operator == "+": # +면
            value = x+y # x + y 값을 저장
        elif operator == "-": # -면
            value = x-y# x - y 값을 저장
            
        # 계산된 value 값을 result와 비교
        if value == result:
            answer += "O" # 같으면 O
        else:
            answer += "X" # 틀리면 X
    return answer