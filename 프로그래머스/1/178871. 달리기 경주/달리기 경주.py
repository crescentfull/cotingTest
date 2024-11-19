def solution(players, callings):
    # 선수 이름과 인덱스를 매핑하는 딕셔너리 생성
    player_index = {player: idx for idx, player in enumerate(players)}

    for calling in callings:
        # 추월한 선수의 현재 위치
        current_idx = player_index[calling]

        if current_idx > 0:  # 1등은 추월할 수 없음
            # 바로 앞 선수와의 위치 교환
            prev_idx = current_idx - 1
            prev_player = players[prev_idx]

            # 배열에서 위치 교환
            players[current_idx], players[prev_idx] = players[prev_idx], players[current_idx]

            # 해시 테이블 업데이트
            player_index[calling] = prev_idx
            player_index[prev_player] = current_idx

    return players
