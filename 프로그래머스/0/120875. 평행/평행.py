def solution(dots):
    # 두 점을 선택하여 직선의 기울기를 비교합니다.
    def slope(dot1, dot2):
        return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
    
    # 네 점에서 만들 수 있는 모든 두 직선의 기울기를 비교합니다.
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    
    # 평행한 직선이 없다면 0을 반환합니다.
    return 0