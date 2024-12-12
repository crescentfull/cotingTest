def solution(nums):
    # N: 전체 폰켓몬 마리 수 (항상 짝수)
    N = len(nums)
    # N/2마리를 선택 가능
    half = N // 2
    
    # set으로 만들어서 unique한 종류의 개수 파악
    unique_types = len(set(nums))
    
    # "가능한 종류 수"는 고유 종류 수와 N/2 중 더 작은 값
    # - 만약 unique_types가 N/2보다 많다면, 실제로 N/2마리밖에 못 뽑으므로 최대 종류 수는 N/2
    # - unique_types가 N/2보다 작거나 같다면, unique_types만큼 종류를 모두 다르게 뽑을 수 있다.
    return min(unique_types, half)
