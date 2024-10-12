def solution(s):
    answer = []
    last_seen = {}  # 문자의 마지막 등장 위치를 기록하는 딕셔너리

    for i, char in enumerate(s):
        if char in last_seen:
            # 현재 위치에서 이전에 등장한 위치를 뺀 값을 저장
            answer.append(i - last_seen[char])
        else:
            # 이전에 등장한 적이 없다면 -1을 저장
            answer.append(-1)
        
        # 현재 문자의 마지막 등장 위치를 업데이트
        last_seen[char] = i

    return answer