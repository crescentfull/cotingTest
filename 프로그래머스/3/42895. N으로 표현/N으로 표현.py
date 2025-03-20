def solution(N, number):
    # 숫자 N을 이용해 number를 만들되, 최소 횟수로 만드는 방법을 찾아야함
    # +,-,*,/ 연산만 가능
    # N을 여러 개 조합해서 새로운 숫자를 만들어야 함
    # N을 최대 8번까지만 사용할 수 있음. 그 이상이면 -1을 반환
    
    # 접근 방식 
    # dp를 이용한 set연산
    # N을 몇 번 사용했을 때 만들 수 있는 숫자들을 저장하는 방식으로 
    answer = 0
    
    if N == number:
        answer = 1
        return answer
    
    dp = [set() for _ in range(9)]
    
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2) # 덧셈
                    dp[i].add(num1 - num2) # 뺄셈
                    dp[i].add(num1 * num2) # 곱셈
                    if num2 != 0:
                        dp[i].add(num1 // num2) # 나누기 (정수 나누기)
        if number in dp[i]:
            answer = i
            return answer
    return -1