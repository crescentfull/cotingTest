def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]  # 조카가 발음할 수 있는 단어 목록
    answer = 0  # 발음할 수 있는 단어 개수를 저장할 변수

    # 입력된 각 문자열을 검사
    for word in babbling:
        for sound in valid_sounds:
            # 발음할 수 있는 소리를 빈 문자열로 대체하여 제거
            if sound * 2 not in word:  # 같은 발음이 연속으로 두 번 등장하면 안됨
                word = word.replace(sound, ' ')
        
        # 모든 유효한 발음을 제거한 후 남은 문자열이 없어야 발음할 수 있는 단어
        if word.strip() == "":
            answer += 1

    return answer  # 최종적으로 발음할 수 있는 단어 개수 반환