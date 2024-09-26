from itertools import combinations

def solution(number):
    count = 0
    # 모든 3명의 조합을 탐색
    for trio in combinations(number, 3):
        if sum(trio) == 0:  # 합이 0인 경우
            count += 1
    return count
