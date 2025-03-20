# 메모리 최적화를 위한 코드 & 테스트케이스

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

def solution2(genres, plays):
  '''
  장르별 재생 횟수 저장 -> 중첩리스트 제거
  장르별 노래 저장 -> 단일 리스트(songs)사용,dict를 제거하여 메모리 사용 최소화
  정렬 방식 -> 삽입정렬 사용, sorted()없이 직접 정렬 수행
  최대 2곡 선택 -> count 기반 선형 탐색 , 슬라이싱 없이 count로 2곡 선택
  '''
    n = len(genres)

    # 1. (고유 번호, 장르, 재생 횟수) 리스트 생성
    songs = [(i, genres[i], plays[i]) for i in range(n)]

    # 2. 장르별 총 재생 횟수 계산
    genre_play_count = {}
    for _, genre, play in songs:
        if genre in genre_play_count:
            genre_play_count[genre] += play
        else:
            genre_play_count[genre] = play

    # 3. 장르별 총 재생 횟수 내림차순 정렬 (삽입 정렬 사용)
    sorted_genres = list(genre_play_count.keys())
    for i in range(1, len(sorted_genres)):
        key = sorted_genres[i]
        j = i - 1
        while j >= 0 and genre_play_count[sorted_genres[j]] < genre_play_count[key]:
            sorted_genres[j + 1] = sorted_genres[j]
            j -= 1
        sorted_genres[j + 1] = key

    # 4. (재생 횟수 내림차순, 고유 번호 오름차순)으로 정렬 (삽입 정렬 사용)
    for i in range(1, len(songs)):
        key = songs[i]
        j = i - 1
        while j >= 0 and (songs[j][2] < key[2] or (songs[j][2] == key[2] and songs[j][0] > key[0])):
            songs[j + 1] = songs[j]
            j -= 1
        songs[j + 1] = key

    # 5. 장르별 최대 2개씩 선택
    answer = []
    for genre in sorted_genres:
        count = 0
        for song in songs:
            if song[1] == genre:
                answer.append(song[0])
                count += 1
                if count == 2:
                    break

    return answer

def solution3(genres, plays):
    '''
    삽입 정렬 -> sorted()
    sort() 사용
    불필요 변수 제거(추가적인 반복문 제거)
    '''
    n = len(genres)

    # 1. (고유 번호, 장르, 재생 횟수) 리스트 생성
    songs = [(i, genres[i], plays[i]) for i in range(n)]

    # 2. 장르별 총 재생 횟수 계산 (딕셔너리 대신 리스트 활용)
    genre_play_count = {}
    for _, genre, play in songs:
        if genre in genre_play_count:
            genre_play_count[genre] += play
        else:
            genre_play_count[genre] = play

    # 3. 장르별 총 재생 횟수 내림차순 정렬 (메모리 절약을 위해 리스트 변환 후 정렬)
    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)

    # 4. (재생 횟수 내림차순, 고유 번호 오름차순)으로 전체 정렬
    # - 재생 횟수가 많은 순서대로 정렬
    # - 같은 재생 횟수라면 고유 번호가 낮은 순서
    songs.sort(key=lambda x: (-x[2], x[0]))

    # 5. 장르별 최대 2개씩 선택
    answer = []
    for genre in sorted_genres:
        count = 0
        for song in songs:
            if song[1] == genre:
                answer.append(song[0])
                count += 1
                if count == 2:
                    break

    return answer

### test
import time

def run_tests():
    test_cases = [
        # 1️⃣ 기본 케이스 (문제에서 제공된 예제)
        {
            "name": "Basic Case",
            "genres": ["classic", "pop", "classic", "classic", "pop"],
            "plays": [500, 600, 150, 800, 2500],
            "expected": [4, 1, 3, 0]
        },
        # 2️⃣ 한 개의 장르만 존재하는 경우
        {
            "name": "Single Genre Only",
            "genres": ["rock", "rock", "rock", "rock"],
            "plays": [400, 300, 200, 100],
            "expected": [0, 1]
        },
        # 3️⃣ 장르별로 노래가 하나만 있는 경우 (모든 곡 선택)
        {
            "name": "One Song Per Genre",
            "genres": ["rock", "pop", "jazz"],
            "plays": [100, 200, 300],
            "expected": [2, 1, 0]
        },
        # 4️⃣ 재생 횟수가 같은 경우 (고유 번호 기준 정렬 확인)
        {
            "name": "Same Play Count, Different IDs",
            "genres": ["hiphop", "hiphop", "hiphop"],
            "plays": [100, 100, 100],
            "expected": [0, 1]
        },
        # 5️⃣ 장르 개수가 최대 100개일 때 (성능 테스트)
        {
            "name": "Maximum Genres",
            "genres": ["genre" + str(i) for i in range(100)],
            "plays": [i for i in range(100)],
            "expected": list(range(99, -1, -1))
        },
        # 6️⃣ 노래 개수가 최대 10,000개일 때 (성능 테스트)
        {
            "name": "Maximum Songs",
            "genres": ["pop"] * 10000,
            "plays": list(range(10000)),
            "expected": [9999, 9998]
        }
    ]

    # 테스트 실행
    for i, case in enumerate(test_cases):
        genres, plays, expected = case["genres"], case["plays"], case["expected"]

        # 실행 시간 측정 시작
        start_time = time.time()
        result = solution2(genres, plays)
        end_time = time.time()

        # 실행 시간 출력
        execution_time = end_time - start_time
        print(f"Test {i+1} ({case['name']}): {'✅ Pass' if result == expected else '❌ Fail'} - {execution_time:.6f} sec")

        # 오류 발생 시 예상 값과 실제 값 출력
        if result != expected:
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

# 실행
run_tests()
