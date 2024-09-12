def solution(picture, k):
    # 결과를 저장할 리스트
    answer = []
    
    # 각 줄을 가로로 k배 확장하고, 세로로도 k배 반복
    for line in picture:
        # 각 문자를 k번 반복하여 새로운 문자열 생성
        expanded_line = ''.join(char * k for char in line)
        # k번 반복하여 세로로 확장
        for _ in range(k):
            answer.append(expanded_line)

    return answer
