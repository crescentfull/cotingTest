def solution(s, n):
    # 결과를 저장할 리스트
    result = []
    
    # 입력 문자열 s의 각 문자를 순회
    for char in s:
        if char == ' ':
            # 현재 문자가 공백이면 그대로 결과에 추가
            result.append(char)
        elif char.islower():
            # 현재 문자가 소문자일 경우
            # ord(char)로 문자의 ASCII 값을 구하고, 'a'의 ASCII 값을 뺀 후 n을 더함
            # 26으로 나눈 나머지를 구해 알파벳 범위를 벗어나지 않도록 함
            # 마지막으로 다시 'a'의 ASCII 값을 더해 새로운 문자의 ASCII 값을 구하고, chr()로 문자 변환
            result.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        elif char.isupper():
            # 현재 문자가 대문자일 경우
            # 소문자와 동일한 방식으로 처리하되, 'A'를 기준으로 변환
            result.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
    
    # 결과 리스트를 문자열로 변환하여 answer에 저장
    answer = ''.join(result)
    
    # 변환된 문자열을 반환
    return answer
