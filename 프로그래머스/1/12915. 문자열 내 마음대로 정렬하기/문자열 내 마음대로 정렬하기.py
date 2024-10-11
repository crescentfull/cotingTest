def solution(strings, n):
    # n번째 문자를 기준으로, 그 문자가 같다면 전체 문자열을 기준으로 정렬
    return sorted(strings, key=lambda x: (x[n], x))