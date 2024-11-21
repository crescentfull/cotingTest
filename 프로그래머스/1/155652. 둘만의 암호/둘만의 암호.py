def solution(s, skip, index):
    # 1. 알파벳 리스트 생성 (skip에 포함된 문자 제외)
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    
    # 2. 변환된 문자열 생성
    result = []
    for char in s:
        # 현재 문자의 위치
        current_idx = alphabet.index(char)
        # index만큼 이동한 새 위치 (순환 구조)
        new_idx = (current_idx + index) % len(alphabet)
        # 변환된 문자 추가
        result.append(alphabet[new_idx])
    
    # 3. 변환된 문자 리스트를 문자열로 변환하여 반환
    return ''.join(result)
