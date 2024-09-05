def solution(polynomial):
    # 초기 계수 설정
    x_coeff = 0  # 'x' 항의 계수
    constant = 0  # 상수항

    # 공백을 기준으로 문자열을 나누고 각 항을 처리
    terms = polynomial.split(" ")

    # 항을 순회하며 계수 합산
    for term in terms:
        if 'x' in term:  # 일차항인 경우
            if term == 'x':  # "x" 단독일 경우 계수는 1
                x_coeff += 1
            else:  # "ax" 형태일 경우 계수는 숫자 부분
                x_coeff += int(term[:-1])
        elif term.isdigit():  # 상수항인 경우
            constant += int(term)

    # 결과 문자열 구성
    result = []
    if x_coeff > 0:
        if x_coeff == 1:
            result.append("x")  # 계수가 1인 경우 "x"
        else:
            result.append(f"{x_coeff}x")
    if constant > 0:
        result.append(str(constant))

    return " + ".join(result)  # 최종 결과 문자열

