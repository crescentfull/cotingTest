def solution(my_string, overwrite_string, s):
    # my_string의 s 이전 부분 + overwrite_string + 나머지 부분을 이어붙여서 반환
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return answer
