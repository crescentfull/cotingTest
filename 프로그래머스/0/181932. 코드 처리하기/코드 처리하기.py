def solution(code):
    mode = 0  # 시작할 때 mode는 0
    ret = ""  # 결과를 저장할 문자열

    # 문자열을 앞에서부터 순회하면서 각 문자 처리
    for idx in range(len(code)):
        # mode가 0일 때의 처리
        if mode == 0:
            if code[idx] == "1":
                mode = 1  # 현재 문자가 "1"이면 mode를 1로 변경
            elif idx % 2 == 0:
                ret += code[idx]  # "1"이 아니고, 짝수 인덱스일 때 ret에 추가
        # mode가 1일 때의 처리
        else:
            if code[idx] == "1":
                mode = 0  # 현재 문자가 "1"이면 mode를 0으로 변경
            elif idx % 2 == 1:
                ret += code[idx]  # "1"이 아니고, 홀수 인덱스일 때 ret에 추가

    # 결과 문자열이 빈 문자열일 경우 "EMPTY" 반환
    return ret if ret else "EMPTY"
