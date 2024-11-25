def solution(wallpaper):
    # 모든 행과 열을 탐색하면서 '#'이 위치한 좌표를 찾음
    rows = [i for i in range(len(wallpaper)) for j in range(len(wallpaper[0])) if wallpaper[i][j] == "#"]
    cols = [j for i in range(len(wallpaper)) for j in range(len(wallpaper[0])) if wallpaper[i][j] == "#"]
    
    # 최소/최대 행과 열 계산
    return [min(rows), min(cols), max(rows) + 1, max(cols) + 1]

# def solution(wallpaper):
#     # 파일 위치의 좌표를 저장할 리스트
#     rows, cols = len(wallpaper), len(wallpaper[0])  # wallpaper의 행(row)과 열(col)의 개수를 계산
#     min_row, min_col = rows, cols  # 파일이 있는 최소 행과 최소 열을 찾기 위한 초기값 (최대값으로 설정)
#     max_row, max_col = 0, 0  # 파일이 있는 최대 행과 최대 열을 찾기 위한 초기값 (최소값으로 설정)
    
#     # 모든 파일의 좌표를 확인하여 최솟값 및 최댓값 계산
#     for i in range(rows):  # 각 행(row)을 순회
#         for j in range(cols):  # 각 열(col)을 순회
#             if wallpaper[i][j] == "#":  # 현재 위치에 파일이 있다면
#                 min_row = min(min_row, i)  # 최소 행 값을 업데이트
#                 min_col = min(min_col, j)  # 최소 열 값을 업데이트
#                 max_row = max(max_row, i)  # 최대 행 값을 업데이트
#                 max_col = max(max_col, j)  # 최대 열 값을 업데이트
    
#     # 드래그는 직사각형이므로 마지막 좌표에 1을 더함
#     # 시작점: (min_row, min_col), 끝점: (max_row + 1, max_col + 1)
#     return [min_row, min_col, max_row + 1, max_col + 1]
