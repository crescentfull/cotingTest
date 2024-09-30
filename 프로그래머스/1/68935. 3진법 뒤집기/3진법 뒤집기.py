def solution(n):
    answer = 0
    # 1. 10진법 수를 3진법 문자열로 변환
    # 변환한 3진법을 저장할 변수 초기화
    ternary = ''
    
    # n이 0보다 큰 동안 반복
    while n > 0:
        # n을 3으로 나눈 몫과 나머지를 계산
        # 나머지는 3진법의 현재 자릿수, 몫은 다음 루프에서 사용할 n의 값이 됨
        n, remainder = divmod(n, 3)
        
        # 현재 자릿수의 값을 문자열로 추가 (3진법의 가장 뒤쪽부터 추가됨)
        ternary = str(remainder) + ternary

    # 2. 3진법 문자열을 뒤집음
    # 예를 들어, 45를 3진법으로 변환하면 "1200"이 되고, 이를 뒤집으면 "0021"
    reversed_ternary = ternary[::-1]

    # 3. 뒤집힌 3진법 문자열을 10진법으로 변환
    # int() 함수의 두 번째 매개변수에 3을 넣으면 해당 문자열을 3진법으로 해석하여 10진법 정수로 변환함
    answer = int(reversed_ternary, 3)

    # 4. 최종 결과를 반환
    return answer