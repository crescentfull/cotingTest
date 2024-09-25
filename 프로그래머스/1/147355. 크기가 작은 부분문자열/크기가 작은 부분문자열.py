def solution(t, p):
    answer = 0
    count = 0
    len_p = len(p)
    int_p = int(p)  # p를 정수로 변환

    # t에서 p와 길이가 같은 부분문자열 추출 및 비교
    for i in range(len(t) - len_p + 1):
        substring = t[i:i + len_p]  # 부분문자열 추출
        if int(substring) <= int_p:  # 부분문자열을 숫자로 변환 후 비교
            count += 1
    answer = count
    return answer