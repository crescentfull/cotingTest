def solution(ingredient):
    stack = []
    count = 0

    for item in ingredient:
        stack.append(item)
        # 마지막 4개의 원소가 [1, 2, 3, 1] 패턴인지 확인
        if stack[-4:] == [1, 2, 3, 1]:
            # 햄버거 포장
            count += 1
            # 포장된 햄버거의 재료 제거
            del stack[-4:]

    return count