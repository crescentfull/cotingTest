def solution(num, total):
    # 첫 번째 숫자 계산
    # (total - (num * (num - 1)) // 2) // num:
    # 전체 total에서 연속된 숫자들의 증가합(1 + 2 + ... + (num - 1))을 뺀 후 num으로 나누어 첫 번째 숫자를 계산
    start = (total - (num * (num - 1)) // 2) // num
    
    # 연속된 num개의 숫자를 생성하여 리스트에 저장
    # start부터 시작하는 num개의 연속된 숫자들을 리스트로 반환
    answer = [start + i for i in range(num)]
    
    return answer  # 최종 결과 리스트 반환