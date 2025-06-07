def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    print(numbers)
    check = [numbers[0]*numbers[1],numbers[-2]*numbers[-1]]
    answer = max(check)
    return answer