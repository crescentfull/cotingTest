def solution(cipher, code):
    answer = ''
    print(len(cipher))
    for i in range(1,len(cipher)+1):
        if code*i <= len(cipher):
            answer += cipher[(code*i)-1]
    return answer