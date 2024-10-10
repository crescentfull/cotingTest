def solution(arr):
    # 행의 수와 열의 수를 계산
    num_rows = len(arr)
    num_cols = len(arr[0])
    
    # 행의 수가 더 많으면 각 행의 끝에 0을 추가
    if num_rows > num_cols:
        for i in range(num_rows):
            arr[i].extend([0] * (num_rows - num_cols))
    
    # 열의 수가 더 많으면 각 열의 끝에 0으로 채운 행을 추가
    elif num_cols > num_rows:
        for _ in range(num_cols - num_rows):
            arr.append([0] * num_cols)
    
    # 결과 반환
    return arr
