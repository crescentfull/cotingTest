def solution(A, B):
    # A를 여러 번 오른쪽으로 밀어 B와 비교
    for i in range(len(A)):
        # A를 i번 밀었을 때의 결과와 B를 비교
        if A == B:
            return i
        # A를 한 번 오른쪽으로 밀기 (마지막 문자를 앞으로 이동)
        A = A[-1] + A[:-1]
    # B와 같아지지 않으면 -1 반환
    return -1
