def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        if signs[i]:
            total += absolutes[i]  # signs[i]가 True이면 양수
        else:
            total -= absolutes[i]  # signs[i]가 False이면 음수
    return total