from collections import Counter

def solution(k, tangerine):
    # 귤 크기별 개수를 세기
    counter = Counter(tangerine)
    
    # 개수 기준으로 내림차순 정렬
    counts = sorted(counter.values(), reverse=True)
    
    # 필요한 귤 개수 채우기
    total = 0
    kinds = 0
    for count in counts:
        total += count  # 현재 종류의 귤 추가
        kinds += 1      # 선택한 귤의 종류 추가
        if total >= k:  # k개 이상 선택하면 종료
            break
    
    return kinds
