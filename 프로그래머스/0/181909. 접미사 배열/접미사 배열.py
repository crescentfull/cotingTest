def solution(my_string):
    answer = []
    word = ""
    for i in range(len(my_string)):
        word = my_string[i:]
        answer.append(word)
    return sorted(answer)