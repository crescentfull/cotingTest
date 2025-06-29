def solution(num, k):
    answer = -1
    cnt = 0
    str_num = str(num)
    for i in str_num:
        cnt += 1
        if i == str(k):
            answer = cnt
            break;

    return answer