def solution(phone_number):
    answer = ''
    back_digit = phone_number[-4::]
    front_digit = phone_number[:-4]
    new_front_digit = "*"*len(front_digit)
    answer = new_front_digit + back_digit
    print(answer)
    return answer