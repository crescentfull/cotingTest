def solution(arr):
    result = []  
    
    # 첫 번째 원소는 무조건 결과 리스트에 추가
    result.append(arr[0])
    
    # 두 번째 원소부터 이전 원소와 비교하며 처리
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  # 현재 원소와 이전 원소가 다르면
            result.append(arr[i])
    
    return result
