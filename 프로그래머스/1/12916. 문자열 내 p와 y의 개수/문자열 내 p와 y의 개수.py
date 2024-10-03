def solution(s):
    # 대소문자 구분 없이 비교하기 위해 모두 소문자로 변환
    s = s.lower()
    
    # 'p'와 'y'의 개수를 각각 센다
    count_p = s.count('p')
    count_y = s.count('y')
    
    # 'p'의 개수와 'y'의 개수가 같으면 True, 다르면 False를 반환
    answer = count_p == count_y
    return answer
