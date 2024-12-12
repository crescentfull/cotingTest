def solution(phone_book):
    # 1. 전화번호 리스트 정렬
    phone_book.sort()
    
    # 2. 정렬된 리스트에서 인접한 두 전화번호를 비교
    #    만약 phone_book[i]가 phone_book[i+1]의 접두어이면 False 반환
    for i in range(len(phone_book) - 1):
        # 현재 번호와 다음 번호를 꺼냄
        current = phone_book[i]
        next_num = phone_book[i+1]
        
        # startswith()를 사용해 접두어 관계 확인
        if next_num.startswith(current):
            return False
    
    # 모든 비교를 통과하면 접두어 관계 없음
    return True