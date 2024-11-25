def solution(wallpaper):
    # 모든 행과 열을 탐색하면서 '#'이 위치한 좌표를 찾음
    rows = [i for i in range(len(wallpaper)) for j in range(len(wallpaper[0])) if wallpaper[i][j] == "#"]
    cols = [j for i in range(len(wallpaper)) for j in range(len(wallpaper[0])) if wallpaper[i][j] == "#"]
    
    # 최소/최대 행과 열 계산
    return [min(rows), min(cols), max(rows) + 1, max(cols) + 1]