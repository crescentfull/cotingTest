import math

def solution(arr):
    # 두 수의 최소공배수를 구하는 함수
    def lcm(a, b):
        return a * b // math.gcd(a, b)  # math.gcd를 이용하여 최소공배수 계산

    # 리스트의 모든 원소의 최소공배수를 순차적으로 계산
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)  # 현재까지의 LCM과 다음 숫자의 LCM 계산
    return result
