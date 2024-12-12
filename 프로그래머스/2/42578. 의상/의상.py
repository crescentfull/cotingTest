def solution(clothes):
    # 종류별로 의상의 수를 세기 위한 딕셔너리
    category_dict = {}
    
    for name, category in clothes:
        # 각 의상의 종류(category)를 key로 하여 개수를 센다.
        if category in category_dict:
            category_dict[category] += 1
        else:
            category_dict[category] = 1
    
    # 모든 종류를 곱셈하기 위한 초기값
    # (각 종류별 경우의 수: 의상 개수 + 1)
    # 최종적으로 (카테고리1의 경우의 수) * (카테고리2의 경우의 수) * ... - 1
    # -1은 모든 종류에서 아무것도 고르지 않은 경우를 제외하기 위함
    result = 1
    
    for category, count in category_dict.items():
        # 해당 카테고리의 경우의 수 = count(의상 수) + 1(아무것도 안 고름)
        result *= (count + 1)
    
    # 아무것도 고르지 않은 경우를 제외
    result -= 1
    
    return result

# 테스트
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 예제1: 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))           # 예제2: 3
