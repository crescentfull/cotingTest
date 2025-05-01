def solution(sides):
    answer = 0
    longest_side = max(sides)
    sides.remove(longest_side)
    other_sides = sum(sides)
    
    if longest_side < other_sides:
        answer = 1
    elif longest_side >= other_sides: 
        answer = 2
    
    return answer