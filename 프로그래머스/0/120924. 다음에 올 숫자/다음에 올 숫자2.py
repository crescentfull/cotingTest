def solution(common):
    answer = 0
    # 첫 번째와 두 번째 수의 차이 계산 (공차)
    diff = common[1] - common[0]
    
    # 등차수열인지 확인
    if common[2] - common[1] == diff:
        # 등차수열이라면 다음 값은 마지막 값에 공차를 더한 값
        answer = common[-1] + diff
    else:
        # 등비수열 확인 (common[0]이 0이 아니거나 공비 계산을 위해 common[1]이 0인 경우도 고려)
        if common[0] != 0:
            ratio = common[1] / common[0]
        else:
            ratio = common[2] / common[1]  # common[0]이 0이면 common[1]을 기준으로 공비 계산
            
        if common[1] * ratio == common[2]:
            # 등비수열이라면 다음 값은 마지막 값에 공비를 곱한 값
            answer = common[-1] * ratio
    return int(answer)
