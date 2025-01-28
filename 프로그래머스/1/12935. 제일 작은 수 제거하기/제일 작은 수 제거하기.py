def solution(arr):
    # 배열의 길이가 1인 경우, [-1]을 반환
    if len(arr) == 1:
        return [-1]
    
    # 배열에서 가장 작은 값 찾기
    min_value = min(arr)
    
    # 가장 작은 값을 제거한 새로운 배열 생성
    result = [num for num in arr if num != min_value]
    
    return result