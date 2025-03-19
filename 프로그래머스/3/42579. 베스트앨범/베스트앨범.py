def solution(genres, plays):
    # 1. 장르별 총 재생 횟수 계산
    genre_play_dict = {}  # {장르: 총 재생 횟수}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in genre_play_dict:
            genre_play_dict[genre] += play
        else:
            genre_play_dict[genre] = play

    # 2. 장르별 노래 저장
    song_dict = {}  # {장르: [(재생 횟수, 고유 번호)]}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in song_dict:
            song_dict[genre].append((play, i))
        else:
            song_dict[genre] = [(play, i)]

    # 3. 장르를 재생 횟수 내림차순으로 정렬 (선택 정렬 구현)
    sorted_genres = list(genre_play_dict.keys())  # 장르 리스트 만들기
    for i in range(len(sorted_genres) - 1):
        max_idx = i
        for j in range(i + 1, len(sorted_genres)):
            if genre_play_dict[sorted_genres[j]] > genre_play_dict[sorted_genres[max_idx]]:
                max_idx = j
        sorted_genres[i], sorted_genres[max_idx] = sorted_genres[max_idx], sorted_genres[i]

    # 4. 장르 내에서 (재생 횟수 내림차순, 고유 번호 오름차순) 정렬 (버블 정렬 구현)
    for genre in song_dict:
        songs = song_dict[genre]
        n = len(songs)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                # 재생 횟수가 같으면 고유 번호 오름차순
                if songs[j][0] < songs[j + 1][0] or (songs[j][0] == songs[j + 1][0] and songs[j][1] > songs[j + 1][1]):
                    songs[j], songs[j + 1] = songs[j + 1], songs[j]

    # 5. 정렬된 순서대로 최대 2곡 선택
    answer = []
    for genre in sorted_genres:
        songs = song_dict[genre]
        count = 0
        for song in songs:
            answer.append(song[1])  # 고유 번호 추가
            count += 1
            if count == 2:  # 최대 2곡까지만 추가
                break

    return answer
