def solution(numbers, hand):
    # 키패드에서 각 숫자(및 *, #)의 위치 (row, col)를 미리 정의합니다.
    #   1,2,3
    #   4,5,6
    #   7,8,9
    #   *,0,#
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 왼손과 오른손 엄지손가락의 초기 위치
    left_pos = keypad['*']   # (3, 0)
    right_pos = keypad['#']  # (3, 2)
    
    # 결과를 누적할 문자열
    result = ""
    
    # 숫자를 순회하며 누를 엄지손가락을 결정합니다.
    for num in numbers:
        # 1, 4, 7 => 무조건 왼손
        if num in [1, 4, 7]:
            result += "L"
            left_pos = keypad[num]
        # 3, 6, 9 => 무조건 오른손
        elif num in [3, 6, 9]:
            result += "R"
            right_pos = keypad[num]
        # 2, 5, 8, 0 => 둘 중 더 가까운 손, 거리가 같으면 hand에 따라
        else:
            # 현재 왼손/오른손 위치
            l_row, l_col = left_pos
            r_row, r_col = right_pos
            # 눌러야 할 숫자의 위치
            n_row, n_col = keypad[num]
            
            # 맨해튼 거리로 비교 (상하좌우 이동 1칸당 거리 1)
            left_dist = abs(l_row - n_row) + abs(l_col - n_col)
            right_dist = abs(r_row - n_row) + abs(r_col - n_col)
            
            if left_dist < right_dist:
                result += "L"
                left_pos = keypad[num]
            elif left_dist > right_dist:
                result += "R"
                right_pos = keypad[num]
            else:  # 거리가 같을 때
                if hand == "right":
                    result += "R"
                    right_pos = keypad[num]
                else:  # hand == "left"
                    result += "L"
                    left_pos = keypad[num]
    
    return result
