def solution(a, b):
    # 각 달의 일수를 저장 (윤년이므로 2월은 29일까지)
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 요일 리스트 (금요일부터 시작)
    day_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 누적 일수를 계산 (1월부터 a-1월까지의 합)
    total_days = sum(days_in_month[:a-1]) + b - 1
    
    # 요일 계산
    return day_of_week[total_days % 7]