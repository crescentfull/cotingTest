def solution(numLog):
    answer = ''
    move_map = {
        1: 'w',
        -1: 's',
        10: 'd',
        -10: 'a',
    }
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        answer += move_map[diff]
    return answer