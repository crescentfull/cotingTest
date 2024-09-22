from itertools import product

def generate_candidates(hint):
    """
    첫 번째 힌트에서 '?'가 들어간 자리를 숫자로 대체해 가능한 모든 비밀번호 후보를 생성하는 함수
    """
    # '?'를 대체할 수 있는 숫자들의 리스트
    possible_replacements = [str(i) for i in range(10)]
    # '?'가 있는 자리마다 숫자들을 대체하기 위한 product 사용
    slots = [(possible_replacements if char == '?' else [char]) for char in hint]
    return [''.join(p) for p in product(*slots)]

def is_invalid(candidate, hint):
    """
    특정 후보 비밀번호가 두 번째 힌트의 패턴과 일치하는지 확인하는 함수
    """
    for i in range(len(hint)):
        if hint[i] != '?' and hint[i] != candidate[i]:
            return False
    return True

def solution(hint1, hint2):
    # 첫 번째 힌트를 기반으로 가능한 모든 비밀번호 후보 생성
    candidates = generate_candidates(hint1)
    
    # 두 번째 힌트에서 비밀번호가 아닌 후보들을 필터링
    invalid_candidates = set()
    for h in hint2:
        # 두 번째 힌트에 해당하는 가능한 모든 패턴 생성
        invalids = generate_candidates(h)
        invalid_candidates.update(invalids)  # 불가능한 비밀번호 후보 추가
    
    # 가능한 후보들에서 비밀번호가 아닌 것들을 제외
    valid_candidates = [c for c in candidates if c not in invalid_candidates]
    
    # 결과를 오름차순으로 정렬
    return sorted(valid_candidates)

# 테스트
hint1 = "0123??"
hint2 = ["12????", "??7?89"]
print(solution(hint1, hint2))
