def solution(numlist, n):
    # 정수 배열 numlist를 n으로부터 가까운 순서대로 정렬하고,
    # 거리가 같을 경우 더 큰 수가 앞에 오도록 정렬
    # sorted() 함수를 사용하여 두 가지 기준으로 정렬:
    # 첫 번째 기준: n으로부터의 거리 오름차순 (abs(x - n))
    # 두 번째 기준: 거리가 같으면 더 큰 숫자가 앞에 오도록 내림차순 (-x)
    answer = sorted(numlist, key=lambda x: (abs(x - n), -x))
    
    return answer
