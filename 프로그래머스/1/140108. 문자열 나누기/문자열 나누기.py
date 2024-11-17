def solution(s):
    count = 0  # 분리된 문자열의 개수
    i = 0  # 문자열을 탐색할 인덱스

    while i < len(s):
        x = s[i]  # 현재 문자열의 첫 글자
        x_count = 0  # x의 등장 횟수
        other_count = 0  # x가 아닌 다른 글자의 등장 횟수

        # 문자열을 왼쪽에서 오른쪽으로 읽으며 x와 다른 글자의 등장 횟수를 센다
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            i += 1

            # x와 다른 글자의 횟수가 같아지면 분리
            if x_count == other_count:
                break

        count += 1  # 분리된 문자열 개수 증가

    return count