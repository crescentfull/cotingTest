def solution(numbers):
    result = set()  # 중복을 자동으로 제거하기 위해 집합(set)을 사용
    
    length = len(numbers)  # numbers 배열의 길이를 저장하여 반복문에서 사용
    
    # 이중 for문으로 서로 다른 두 수의 합을 구함
    for i in range(length):
        for j in range(i + 1, length):  # i 다음부터 시작하여 중복되지 않도록 처리
            sum_value = numbers[i] + numbers[j]  # numbers[i]와 numbers[j]의 합을 구함
            result.add(sum_value)  # 집합에 합을 추가 (중복된 값은 자동으로 제거됨)
    
    # 최종적으로 집합을 리스트로 변환하고 오름차순으로 정렬하여 반환
    return sorted(result)