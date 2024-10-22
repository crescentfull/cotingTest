def solution(food):
    result = []
    
    # 1번 음식부터 시작하므로 food[1:]을 순회
    for i in range(1, len(food)):
        # 각 음식의 개수를 2로 나누어 좌우에 배치할 수 있는 양을 계산
        count = food[i] // 2
        # 좌측에 해당 음식 개수를 추가
        result.append(str(i) * count)
    
    # 좌측 부분과 그 역순으로 대칭을 이루는 우측 부분을 결합하고, 중앙에 물(0)을 넣는다
    return ''.join(result) + '0' + ''.join(result[::-1])
