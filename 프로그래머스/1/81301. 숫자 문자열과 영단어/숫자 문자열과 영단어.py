def solution(s):
    # 숫자와 영단어 매핑
    num_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    # 영단어를 숫자로 변환
    for word, num in num_words.items():
        s = s.replace(word, num)
    
    # 변환된 문자열을 정수로 반환
    return int(s)