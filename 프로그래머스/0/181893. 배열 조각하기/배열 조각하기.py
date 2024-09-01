def solution(arr, query):
    answer = [] 

    # query 배열을 순회하면서 작업 수행
    for i in range(len(query)):
        if i % 2 == 0:  # 짝수 인덱스의 경우
            # query[i]번 인덱스 이후의 모든 요소를 잘라내기
            # 배열의 앞부분만 유지
            arr = arr[:query[i] + 1]
        else:  # 홀수 인덱스의 경우
            # query[i]번 인덱스 이전의 모든 요소를 잘라내기
            # 배열의 뒷부분만 유지
            arr = arr[query[i]:]

    # 모든 작업이 끝난 후 arr에 최종 결과가 저장됨
    answer = arr  # answer에 최종 결과 저장

    return answer  # 결과 반환

