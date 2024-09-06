def solution(array):
    # 배열을 오름차순으로 정렬
    array.sort()
    
    # 중앙값을 구하기 위해 배열 길이의 중간 인덱스를 계산
    mid_index = len(array) // 2
    
    # 중앙값 반환
    return array[mid_index]