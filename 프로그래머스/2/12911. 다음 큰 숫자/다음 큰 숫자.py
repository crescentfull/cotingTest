def solution(n):
    # 주어진 n의 이진수에서 1의 개수를 구함
    count_ones = bin(n).count('1')

    # n보다 큰 숫자를 순차적으로 탐색
    while True:
        n += 1  # 다음 숫자로 증가
        if bin(n).count('1') == count_ones:  # 1의 개수가 같은 경우
            answer = n  # 결과값 저장
            break  # 가장 작은 수를 찾았으므로 종료

    return answer
