from collections import deque

def solution(picks, minerals):
    fatigue_table = {
        'diamond': {'diamond':1, 'iron':1, 'stone':1 },
        'iron':    {'diamond':5, 'iron':1, 'stone':1 },
        'stone':   {'diamond':25,'iron':5,'stone':1 }
    }
    
    dq = deque(minerals)
    
    sets = []
    while dq:
        # 남은 광물이 len(dq)개
        # 5개 또는 남은 개수 중 작은 값만큼 popleft()
        chunk_size = min(5, len(dq))
        chunk = [dq.popleft() for _ in range(chunk_size)]
        
        dia_count = chunk.count('diamond')
        iron_count = chunk.count('iron')
        stone_count = chunk.count('stone')
        sets.append((dia_count, iron_count, stone_count))

    from functools import lru_cache

    @lru_cache(None)
    def dfs(index, d_left, i_left, s_left):
        # index번째 세트부터 끝까지 채굴
        if index == len(sets):
            return 0
        
        dia_c, iron_c, stone_c = sets[index]
        
        # 곡괭이 없으면 더이상 채굴 불가, 남은 광물 무시
        if d_left == 0 and i_left == 0 and s_left == 0:
            return 0
        
        res = float('inf')
        
        # 다이아 곡괭이 사용
        if d_left > 0:
            cost = (fatigue_table['diamond']['diamond'] * dia_c
                    + fatigue_table['diamond']['iron'] * iron_c
                    + fatigue_table['diamond']['stone'] * stone_c)
            res = min(res, cost + dfs(index+1, d_left-1, i_left, s_left))
        
        # 철 곡괭이 사용
        if i_left > 0:
            cost = (fatigue_table['iron']['diamond'] * dia_c
                    + fatigue_table['iron']['iron'] * iron_c
                    + fatigue_table['iron']['stone'] * stone_c)
            res = min(res, cost + dfs(index+1, d_left, i_left-1, s_left))
        
        # 돌 곡괭이 사용
        if s_left > 0:
            cost = (fatigue_table['stone']['diamond'] * dia_c
                    + fatigue_table['stone']['iron'] * iron_c
                    + fatigue_table['stone']['stone'] * stone_c)
            res = min(res, cost + dfs(index+1, d_left, i_left, s_left-1))
        
        return res

    return dfs(0, picks[0], picks[1], picks[2])