def solution(bandage, health, attacks):
    t, x, y = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    max_health = health  # 최대 체력
    current_health = health  # 현재 체력
    success_time = 0  # 연속 성공 시간
    attack_index = 0  # 공격 인덱스
    attack_count = len(attacks)  # 공격 횟수
    
    # 게임은 최대 공격 시간까지 진행됨
    for time in range(1, 1001):
        # 몬스터의 공격 시간이 되면 체력이 줄어듦
        if attack_index < attack_count and attacks[attack_index][0] == time:
            damage = attacks[attack_index][1]
            current_health -= damage  # 피해량만큼 체력 감소
            attack_index += 1
            success_time = 0  # 기술이 취소되므로 연속 성공 시간 초기화
            
            # 체력이 0 이하로 떨어지면 캐릭터는 죽음
            if current_health <= 0:
                return -1
        else:
            # 붕대 감기 기술을 사용 중
            current_health = min(current_health + x, max_health)  # 초당 회복량만큼 체력 회복
            success_time += 1  # 연속 성공 시간 증가
            
            # 성공 시간이 t초가 되면 추가 회복량 적용
            if success_time == t:
                current_health = min(current_health + y, max_health)  # 추가 회복량 회복
                success_time = 0  # 연속 성공 시간 초기화
        
        # 공격이 끝난 후 남은 체력 반환
        if attack_index >= attack_count and time >= attacks[-1][0]:
            break

    return current_health
