def solution(num):
    # 주어진 수가 이미 1이라면 0을 반환
    if num == 1:
        return 0
    
    count = 0  # 반복 횟수를 저장할 변수

    while num != 1:  # num이 1이 될 때까지 반복
        if num % 2 == 0:  
            num //= 2  # 짝수인 경우 2로 나누기
        else:
            num = num * 3 + 1  # 홀수인 경우 3을 곱하고 1을 더하기
        
        count += 1  # 반복 횟수 증가

        if count >= 500:  # 500번 이상 반복하면 -1 반환
            return -1

    return count  # 1이 될 때까지의 반복 횟수 반환
