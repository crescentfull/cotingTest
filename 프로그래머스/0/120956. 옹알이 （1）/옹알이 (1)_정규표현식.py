'''
최적화 검토
주어진 제한사항을 만족하는 입력에서는 문제가 발생하지 않지만, 만약 문자열 길이나 babbling의 길이가 매우 커진다면, 다른 최적화 방법을 고려해야 할 수도 있음
>>> 정규표현식 사용
'''
import re

def solution(babbling):
    # 정규 표현식 패턴: "aya", "ye", "woo", "ma"가 한 번씩만 사용되고 반복되지 않는 패턴
    pattern = re.compile(r'^(aya|ye|woo|ma)+$')
    answer = 0  # 발음할 수 있는 단어 개수를 저장할 변수

    # 각 문자열을 검사
    for word in babbling:
        # 정규 표현식 패턴에 맞는지 검사
        if pattern.match(word):
            answer += 1

    return answer 

'''
< 주요 코드 풀이 >
- 정규 표현식 패턴:
^(aya|ye|woo|ma)+$는 문자열의 시작(^)부터 끝($)까지 "aya", "ye", "woo", "ma" 중 하나가 한 번 이상 반복되어 나타나는 경우를 찾는다.

- pattern.match(word):
word가 정규 표현식 패턴에 완전히 매칭되는지 검사 -> 매칭되면 None이 아닌 값이 반환되므로, 이를 통해 발음할 수 있는 단어인지 확인할 수 있다.
'''
