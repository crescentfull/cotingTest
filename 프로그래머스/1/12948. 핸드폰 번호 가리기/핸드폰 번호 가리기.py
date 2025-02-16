def solution(phone_number):
    answer = ''
    # 전화번호의 길이를 구함
    length = len(phone_number)
    
    # 전화번호의 뒷 4자리를 제외한 나머지를 '*'로 변환
    masked_part = '*' * (length - 4)
    
    # 전화번호의 뒷 4자리
    visible_part = phone_number[-4:]
    
    # 두 부분을 결합하여 answer 변수에 저장
    answer = masked_part + visible_part
    
    return answer