def solution(array):
    # 초기화
    answer = 0 
    number = 0 # 숫자 변수
    max_count = 0 # 최빈값 
    numberCount = {} # 숫자 횟수 저장할 딕셔너리 생성
    
    # 숫자 횟수 카운트하기 위한 반복문
    for i in array:
        if i in numberCount:
            numberCount[i] += 1
        else:
            numberCount[i] = 1
    
    # 최빈값 찾기
    max_count = max(numberCount.values()) # 가장 많은 횟수 저장
    number = [key for key, value in numberCount.items() if value == max_count] # 가장 많은 횟수를 가진 숫자를 리스트로 저장
    
    # 최빈 값이 여러개일 경우와 그렇지 않은 경우에 대한 판별문
    if len(number) > 1: # 1보다 높다면 number 리스트의 값이 여러개이기 때문에 
        return -1 # -1 반환
    else: # 그렇지 않다면 1개만 있으므로
        answer = number[0] # 0번 인덱스의 값만 answer에 저장해야 리스트로 담겨지지 않는다.
        print(type(answer)) # 정수로 담겨진것 확인
        return answer # 반환
    return answer