def solution(array, commands):
    answer = []
    
    # 각 command에 대해 연산을 수행
    for command in commands:
        i, j, k = command
        # array의 i번째부터 j번째까지 자르고, 정렬
        sliced_array = sorted(array[i-1:j])
        # 정렬된 배열에서 k번째 숫자를 result에 추가
        answer.append(sliced_array[k-1])
    
    return answer