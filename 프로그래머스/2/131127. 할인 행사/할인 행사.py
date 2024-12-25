def solution(want, number, discount):
    # 1. 필요한 제품들의 빈도 수 딕셔너리 만들기
    need = {}
    for w, num in zip(want, number):
        need[w] = num
    
    # 결과(가능한 시작 일자 수)
    answer = 0
    
    # 할인 리스트의 총 길이
    n = len(discount)
    # 만약 discount가 10일 미만이면 바로 0 반환
    if n < 10:
        return 0
    
    # 2. 0 ~ n-10까지 슬라이딩 윈도우 이동
    for start_idx in range(n - 10 + 1):
        # start_idx 부터 start_idx+9까지 10일간 구매할 제품 목록
        window = discount[start_idx:start_idx+10]
        
        # 윈도우 내 제품 빈도 수 세기
        current_freq = {}
        for item in window:
            current_freq[item] = current_freq.get(item, 0) + 1
        
        # 3. need 조건 충족 여부 확인
        #    모든 제품에 대해 current_freq가 need보다 크거나 같은지 검사
        can_buy_all = True
        for item, required_count in need.items():
            # 윈도우에 해당 item이 없거나, 수량이 부족하면 실패
            if current_freq.get(item, 0) < required_count:
                can_buy_all = False
                break
        
        if can_buy_all:
            answer += 1
    
    return answer
