def solution(board, moves):
    basket = []  # 인형을 담을 바구니
    removed_count = 0  # 터뜨려진 인형의 개수

    # 크레인 작업 수행
    for move in moves:
        col = move - 1  # 인덱스는 0부터 시작하므로, 1을 빼줌
        for row in range(len(board)):
            if board[row][col] != 0:  # 해당 열에서 인형이 있으면
                picked = board[row][col]  # 인형을 집음
                board[row][col] = 0  # 해당 위치를 빈 칸으로 설정
                
                # 바구니의 마지막 인형과 같으면 터뜨림
                if basket and basket[-1] == picked:
                    basket.pop()  # 바구니에서 마지막 인형 제거
                    removed_count += 2  # 터뜨려진 인형은 2개
                else:
                    basket.append(picked)  # 바구니에 인형 추가
                break  # 한 번 집으면 해당 열 탐색 종료
    
    return removed_count