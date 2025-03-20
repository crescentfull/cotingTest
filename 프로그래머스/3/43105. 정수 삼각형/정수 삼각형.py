# 삼각형의 꼭대기(triangle[0][0])에서 시작해서 아래층으로 이동하면서 최대 합을 찾아야함
# 이동할 때는 대각선 방향으로 한 칸 왼쪽 또는 오른쪽만 가능
# 최종적으로 바닥 층에서 만들 수 있는 최대 합을 구하는 문제
# 점화식 dp[i][i] = triangle[i][i] + max(dp[i+1][j], dp[i+1][j+1])
# i 번째 행의 j번째 원소는 아래층에서 더 큰 값을 선택해서 합산
# 마지막 층에서 바로 윗층으로 갱신하면서 진행

def solution(triangle):
    # 아래층부터 위로 올라가면서 값을 갱신
    for i in range(len(triangle) - 2, -1, -1):  # 마지막 행 전부터 0번째 행까지 역순 탐색
        for j in range(len(triangle[i])):  # 현재 행의 모든 열을 탐색
            # 아래층의 양쪽 값 중 더 큰 값을 현재 위치에 더함
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    # 최종적으로 꼭대기 값이 최대 합
    return triangle[0][0]