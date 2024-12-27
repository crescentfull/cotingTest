def solution(routes):
    # 차량의 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    # 카메라의 수와 마지막 카메라 설치 지점을 초기화
    camera_count = 0
    last_camera = -30001  # 카메라 설치 가능한 최소 지점보다 작게 설정
    
    for route in routes:
        # 차량의 진출 지점이 마지막 카메라 설치 지점보다 뒤에 있다면
        if route[0] > last_camera:
            # 새로운 카메라를 설치
            camera_count += 1
            # 카메라는 차량의 진출 지점에 설치
            last_camera = route[1]
    
    return camera_count
