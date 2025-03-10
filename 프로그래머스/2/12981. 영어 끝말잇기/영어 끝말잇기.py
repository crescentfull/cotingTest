def solution(n, words):
    answer = []
    used_words = set()  # 사용된 단어 저장
    used_words.add(words[0])  # 첫 번째 단어는 무조건 사용됨
    
    for i in range(1, len(words)):
        prev_word, curr_word = words[i-1], words[i]
        
        # 끝말잇기 규칙 위반 또는 중복 단어 사용 확인
        if curr_word in used_words or prev_word[-1] != curr_word[0]:
            answer = [(i % n) + 1, (i // n) + 1]  # 사람 번호, 차례
            return answer

        used_words.add(curr_word)  # 단어 저장

    answer = [0, 0]  # 아무도 탈락하지 않으면 [0, 0] 반환
    return answer