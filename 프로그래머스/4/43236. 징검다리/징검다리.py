def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        prev = 0
        min_dist = float("inf")
        
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
                if removed > n:
                    break
            else:
                min_dist = min(min_dist, rock - prev)
                prev = rock
                
        if removed > n:
            right = mid - 1
        else:
            answer = min_dist
            left = mid + 1
    return answer