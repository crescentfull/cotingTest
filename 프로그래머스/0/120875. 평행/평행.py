def solution(dots):
    # 두 점을 받아 그 사이의 직선의 기울기를 계산하는 함수
    def slope(dot1, dot2):
        # 기울기 공식: (y2 - y1) / (x2 - x1)
        return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
    
    # 네 점에서 가능한 두 직선의 기울기를 비교하여 평행 여부 확인
    # 첫 번째 경우: 점1-점2와 점3-점4를 연결한 직선의 기울기를 비교
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1  # 기울기가 같다면 평행이므로 1을 반환
    
    # 두 번째 경우: 점1-점3과 점2-점4를 연결한 직선의 기울기를 비교
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1  # 기울기가 같다면 평행이므로 1을 반환
    
    # 세 번째 경우: 점1-점4와 점2-점3을 연결한 직선의 기울기를 비교
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1  # 기울기가 같다면 평행이므로 1을 반환
    
    # 위의 세 경우 모두 평행하지 않다면, 평행한 직선이 없으므로 0을 반환
    return 0
