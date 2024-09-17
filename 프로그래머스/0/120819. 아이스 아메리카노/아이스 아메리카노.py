def solution(money):
    answer = []
    # 아메리카노 한 잔의 가격
    price = 5500
    
    # 최대 잔 수와 남은 돈 계산
    max_cups = money // price
    remaining_money = money % price
    
    # 결과 변수 입력
    answer = [max_cups, remaining_money]
    
    return answer