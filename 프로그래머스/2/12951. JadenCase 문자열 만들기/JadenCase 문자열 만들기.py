def solution(s):
    # 문자열을 공백을 기준으로 나누되, 연속된 공백도 유지하기 위해 split(" ") 사용
    words = s.split(" ")
    
    # 각 단어를 JadenCase로 변환하여 리스트로 저장
    jaden_words = [word.capitalize() for word in words]
    
    # 공백을 기준으로 다시 문자열로 결합
    answer = " ".join(jaden_words)
    return answer