def treasure_hunt(n, resources):
    m = len(resources)  # 탐험가의 수
    result = []  # 각 라운드에서 보물을 차지한 탐험가 번호를 저장할 리스트

    for _ in range(n):
        # 현재 자원이 가장 많은 탐험가 찾기 (동점일 경우 번호가 작은 탐험가가 선택됨)
        max_resource = -1
        chosen_explorer = -1
        
        for i in range(m):
            if resources[i] > max_resource:
                max_resource = resources[i]
                chosen_explorer = i
            elif resources[i] == max_resource and i < chosen_explorer:
                chosen_explorer = i

        # 선택된 탐험가가 보물을 차지함
        result.append(max_resource)  # 선택된 탐험가의 남은 자원을 기록

        # 보물을 차지한 탐험가의 자원을 1 감소시킴
        resources[chosen_explorer] -= 1

    return result

# 테스트 예시 1
n = 4
resources = [85, 32, 65, 19]
print(treasure_hunt(n, resources))  # 출력: [66, 33, 32, 20]

# 테스트 예시 2
n = 6
resources = [3, 7, 1]
print(treasure_hunt(n, resources))  # 출력: [4, 3, 2, 1, 1, -1]

