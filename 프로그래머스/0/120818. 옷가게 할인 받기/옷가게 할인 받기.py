def solution(price):
    answer = 0
    if 500000 <= price:
        answer = price-(price*0.2)
    elif 300000 <= price < 500000:
        answer = price-(price*0.1)
    elif 100000 <= price < 300000:
        answer = price-(price*0.05)
    else:
        answer = price
    
    return int(answer)

