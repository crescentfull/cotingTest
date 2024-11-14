import re

def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계: 소문자, 숫자, '-', '_', '.'를 제외한 모든 문자 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 연속된 마침표를 하나의 마침표로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # 4단계: 마침표가 처음이나 끝에 위치하면 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이면 "a"를 대입
    if new_id == '':
        new_id = 'a'
    
    # 6단계: 길이가 16자 이상이면, 첫 15개 문자만 남김
    new_id = new_id[:15].rstrip('.')
    
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
