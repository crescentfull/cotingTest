def solution(diffs, times, limit):
    # n: 퍼즐의 개수
    n = len(diffs)
    
    # 숙련도의 탐색 범위를 설정
    # 최소 숙련도는 1
    # 최대 숙련도는 모든 퍼즐을 한번에 해결 가능한 수준, 즉 가장 높은 난이도를 가진 퍼즐 이상이면 된다.
    left, right = 1, max(diffs)
    
    # can_solve 함수:
    # 입력으로 주어진 숙련도 level일 때 전체 퍼즐을 순서대로 풀었을 때
    # 총 소요 시간이 limit 이하인지 여부를 반환한다.
    def can_solve(level):
        total_time = 0
        
        # 첫 번째 퍼즐 해결:
        # diffs[0] = 1 이므로 level ≥ 1에서 첫 퍼즐은 항상 틀리지 않는다.
        # 첫 퍼즐은 이전 퍼즐이 없으므로 실패 개념도 없다.
        total_time += times[0]
        # 이미 limit 초과하면 바로 False 반환
        if total_time > limit:
            return False
        
        # i=1 부터 n-1번째 퍼즐까지 순서대로 확인
        for i in range(1, n):
            time_cur = times[i]    # 현재 퍼즐을 해결하는데 필요한 시간
            time_prev = times[i-1] # 이전 퍼즐의 시간 (실패시 다시 풀어야 하므로 필요)
            diff = diffs[i]        # 현재 퍼즐의 난이도
            
            if diff <= level:
                # 현재 숙련도가 퍼즐 난이도보다 크거나 같다면, 틀리지 않고 바로 해결
                total_time += time_cur
            else:
                # 현재 숙련도가 퍼즐 난이도보다 낮다면 여러 번 틀림
                gap = diff - level  # 실패 횟수
                
                # 실패할 때마다 소요 시간:
                # (현재 퍼즐 재도전 time_cur) + (이전 퍼즐 재풀이 time_prev)
                # 이를 gap번 반복한 뒤, 마지막에 성공하는데 time_cur가 추가
                cost = gap * (time_cur + time_prev) + time_cur
                total_time += cost
            
            # 중간에 이미 제한시간을 초과했다면 더 볼 필요 없이 False
            if total_time > limit:
                return False
        
        # 모든 퍼즐 해결 완료 후 total_time이 limit 이하이면 True
        return True
    
    # 이진 탐색을 통해 최소 숙련도 탐색
    # left, right 범위 내에서 can_solve(mid)가 True를 만족하는 최솟값을 찾는다.
    answer = right
    while left <= right:
        mid = (left + right) // 2
        
        # mid 숙련도로 퍼즐을 제한시간 내에 모두 풀 수 있는가?
        if can_solve(mid):
            # 가능하다면 더 낮은 숙련도에서도 가능한지 탐색을 계속한다.
            answer = mid
            right = mid - 1
        else:
            # 불가능하다면 숙련도를 더 올려야 한다.
            left = mid + 1
    
    # 최종적으로 answer에는 제한 시간 내에 모든 퍼즐을 해결할 수 있는 최소 숙련도가 담긴다.
    return answer