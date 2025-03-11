def solution(s):
    count_transform = 0  # 이진 변환 횟수
    count_removed_zeros = 0  # 제거된 0의 개수
    
    while s != "1":  # '1'이 될 때까지 반복
        zeros = s.count('0')  # 현재 문자열에서 0의 개수
        count_removed_zeros += zeros  # 제거한 0의 총 개수 추가
        
        s = bin(len(s.replace('0', '')))[2:]  # 0 제거 후 길이를 2진 변환
        count_transform += 1  # 변환 횟수 증가

    answer = [count_transform, count_removed_zeros]
    return answer
