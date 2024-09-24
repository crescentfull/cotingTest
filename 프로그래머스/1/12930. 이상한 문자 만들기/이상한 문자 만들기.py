def solution(s):
    # 문자열을 공백을 기준으로 나눔
    words = s.split(' ')
    
    # 변환된 단어들을 저장할 리스트
    transformed_words = []
    
    # 각 단어에 대해 변환 작업 수행
    for word in words:
        transformed_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                # 짝수 인덱스는 대문자로
                transformed_word += char.upper()
            else:
                # 홀수 인덱스는 소문자로
                transformed_word += char.lower()
        transformed_words.append(transformed_word)
    
    # 변환된 단어들을 공백으로 이어 붙여서 answer에 저장
    answer = ' '.join(transformed_words)
    
    # 결과 반환
    return answer
