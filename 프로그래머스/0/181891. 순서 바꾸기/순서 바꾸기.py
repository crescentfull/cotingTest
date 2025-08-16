def solution(num_list, n):
    left = []
    right = []
    for i in range(len(num_list)):
        if i >= n:
            left.append(num_list[i])
        else:
            right.append(num_list[i])
    return (left+right)