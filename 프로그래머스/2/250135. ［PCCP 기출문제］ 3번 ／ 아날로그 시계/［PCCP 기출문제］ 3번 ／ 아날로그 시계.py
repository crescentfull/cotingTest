def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    duration = end - start

    # 초기 각도
    hour_angle0 = ((h1 % 12) * 30) + (m1 * 0.5) + (s1 / 120)
    minute_angle0 = (m1 * 6) + (s1 * 0.1)
    second_angle0 = s1 * 6

    # 상대 속도
    ds_h = 6 - (1/120)  # 초침-시침 상대속도
    ds_m = 6 - 0.1       # 초침-분침 상대속도

    diff_h = second_angle0 - hour_angle0
    diff_m = second_angle0 - minute_angle0

    # 가능한 t를 찾기 위해 k, n 범위 추정
    # t >= 0:
    #   for hour: 360*k - diff_h >= 0 → k >= diff_h/360
    # t <= duration:
    #   (360*k - diff_h) / ds_h <= duration → k <= (360*k <= diff_h+ds_h*duration)
    # k, n은 대략 수천 번 정도면 충분 (최대 24시간 → 초침-시침 약 2시간마다 겹침)
    # 실제로 24시간 동안 최대 몇 번 겹치는지 계산 가능하지만, 안전하게 큰 범위
    # 그러나 과도한 반복은 비효율적이므로 k,n 범위를 합리적으로 제한.
    
    # 24시간 최대 겹침 수: 
    # 초침-시침: 초침이 시침을 약 65.4545분마다 잡음 → 24시간 = 약 22번
    # 초침-분침: 초침이 분침을 약 65.4545/0.1*0.1 ... 비슷한 빈도 → 대략 1320번?
    # 실제론 더 적음. We can just compute range by bounding.

    times = []

    def add_times(diff, ds, duration):
        results = []
        # k는 정수. k_min, k_max 추정:
        # (360*k - diff) = ds*t
        # t=0일 때 k ~ diff/360
        k_min = int((diff/360) - 1000)  # 여유 범위
        k_max = int((diff + ds * duration)/360 + 1000)
        for k in range(k_min, k_max+1):
            val = (360*k - diff)/ds
            if 0 <= val <= duration:
                results.append(val)
        return results

    hour_times = add_times(diff_h, ds_h, duration)
    minute_times = add_times(diff_m, ds_m, duration)

    # 이제 triple overlap 처리:
    # 두 리스트를 합친 뒤 정렬, 근접한 값이 매우 가까우면 합침
    # 근접 판단 기준: epsilon
    epsilon = 1e-7

    combined = sorted(hour_times + minute_times)
    merged = []
    for t in combined:
        if not merged or abs(merged[-1] - t) > epsilon:
            merged.append(t)
        else:
            # t와 merged[-1]이 매우 가깝다면 triple overlap으로 한 번만 센다.
            # merged[-1] 그대로 두고 새로 추가 안 함
            pass

    return len(merged)
