import heapq

def treasure_hunt(n, resources):
    m = len(resources)  # 탐험가의 수
    result = []  # 결과 리스트 (각 라운드에서 보물을 차지한 탐험가의 남은 자원)

    for _ in range(n):
        # 자원이 가장 많은 탐험가 선택
        max_resource = -1
        chosen_explorer = -1
        
        for i in range(m):
            if resources[i] > max_resource:
                max_resource = resources[i]
                chosen_explorer = i
            elif resources[i] == max_resource and i < chosen_explorer:
                chosen_explorer = i

        # 선택된 탐험가의 남은 자원을 기록 (현재 자원에서 1 감소 후 남은 자원)
        resources[chosen_explorer] -= 1
        result.append(resources[chosen_explorer] + 1)  # 남은 자원을 기록

    return result

# 테스트 예시 1
n = 4
resources = [85, 32, 65, 19]
print(treasure_hunt(n, resources))  # 출력: [66, 33, 32, 20]

# 테스트 예시 2
n = 6
resources = [3, 7, 1]
print(treasure_hunt(n, resources))  # 출력: [4, 3, 2, 1, 1, -1]

