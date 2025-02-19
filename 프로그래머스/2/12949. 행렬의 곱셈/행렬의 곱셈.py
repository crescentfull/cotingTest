def solution(arr1, arr2):
    # 결과 행렬의 크기 결정 (arr1의 행 개수, arr2의 열 개수)
    rows = len(arr1)
    cols = len(arr2[0])
    
    # 결과 행렬 초기화 (모든 원소를 0으로 설정)
    answer = [[0] * cols for _ in range(rows)]
    
    # 행렬 곱셈 수행
    for i in range(rows):  # arr1의 행 순회
        for j in range(cols):  # arr2의 열 순회
            for k in range(len(arr2)):  # arr1의 열과 arr2의 행이 동일
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer