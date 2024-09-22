from datetime import datetime, timedelta

def solution(day, d_day, walks):
    # 요일을 숫자로 매핑 (월요일=0, 화요일=1, ..., 일요일=6)
    days_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    
    # 시작일과 목표일을 datetime으로 변환
    start_date = datetime(2024, 1, 1)  # 2024년 1월 1일
    end_date = datetime.strptime(d_day, "%Y-%m-%d")  # 목표 날짜
    
    # 시작 요일 설정 (입력받은 day 문자열을 숫자로 변환)
    start_day = days_map[day]
    
    # 첫 주의 월요일로부터 몇 걸음을 걸을 수 있는지 계산하기 위해 요일 조정
    current_date = start_date + timedelta(days=(7 - start_day)) if start_day > 4 else start_date
    
    # 초기 설정
    total_walks = 0  # 지금까지 걸은 걸음 수
    daily_base = 10000  # 첫 달 기본 걸음 수
    plus = 0  # 매달 추가될 걸음 수
    
    while current_date <= end_date:
        year = current_date.year
        month = current_date.month
        
        # 현재 달의 첫 번째 월요일 찾기 (해당 월의 첫 날이 주말이면 월요일로 맞춤)
        first_day_of_month = datetime(year, month, 1)
        if first_day_of_month.weekday() >= 5:  # 주말이면
            # 다음 월요일로 이동
            first_monday = first_day_of_month + timedelta(days=(7 - first_day_of_month.weekday()))
        else:
            first_monday = first_day_of_month
        
        # 그 달의 평일만 계산 (월요일~금요일)
        while first_monday.month == month and first_monday <= end_date:
            # 매일 걷는 걸음 수는 10000 + (현재 달에 해당하는 추가 걸음 수)
            daily_walks = daily_base + plus
            
            total_walks += daily_walks  # 그 날 걸음 수 더하기
            
            # 목표 걸음 수를 초과하면 현재 plus 반환
            if total_walks >= walks:
                return plus
            
            # 다음 날로 이동 (월요일부터 금요일까지만 걷기)
            first_monday += timedelta(days=1)
            if first_monday.weekday() >= 5:  # 주말이면 월요일로 이동
                first_monday += timedelta(days=(7 - first_monday.weekday()))
        
        # 다음 달로 이동
        current_date = first_monday
        plus += 1  # 매달 plus 증가
    
    # 목표 걸음 수를 달성할 수 없으면 -1 반환
    return -1

