import time
from collections import Counter

# 패키지를 사용한 코드
def solution_with_counter(a, b, c, d):
    dice = [a, b, c, d]
    count = Counter(dice)
    counts = sorted(count.items(), key=lambda x: -x[1])
    
    if counts[0][1] == 4:
        p = counts[0][0]
        answer = 1111 * p
    elif counts[0][1] == 3:
        p = counts[0][0]
        q = counts[1][0]
        answer = (10 * p + q) ** 2
    elif counts[0][1] == 2 and counts[1][1] == 2:
        p = counts[0][0]
        q = counts[1][0]
        answer = (p + q) * abs(p - q)
    elif counts[0][1] == 2:
        p = counts[0][0]
        q, r = counts[1][0], counts[2][0]
        answer = q * r
    else:
        answer = min(dice)
    
    return answer

# 패키지를 사용하지 않은 코드
def solution_without_counter(a, b, c, d):
    count = [0] * 7
    for num in [a, b, c, d]:
        count[num] += 1
    freq = sorted([(count[i], i) for i in range(1, 7) if count[i] > 0], reverse=True)
    
    if freq[0][0] == 4:
        p = freq[0][1]
        answer = 1111 * p
    elif freq[0][0] == 3:
        p = freq[0][1]
        q = freq[1][1]
        answer = (10 * p + q) ** 2
    elif freq[0][0] == 2 and freq[1][0] == 2:
        p = freq[0][1]
        q = freq[1][1]
        answer = (p + q) * abs(p - q)
    elif freq[0][0] == 2:
        p = freq[0][1]
        q, r = freq[1][1], freq[2][1]
        answer = q * r
    else:
        answer = min(a, b, c, d)
    
    return answer

# 테스트 실행 및 시간 측정
test_cases = [(2, 2, 2, 2), (4, 1, 4, 4), (6, 3, 3, 6), (2, 5, 2, 6), (6, 4, 2, 5)]

start = time.time()
for _ in range(100000):
    for case in test_cases:
        solution_with_counter(*case)
print("With Counter:", time.time() - start)

start = time.time()
for _ in range(100000):
    for case in test_cases:
        solution_without_counter(*case)
print("Without Counter:", time.time() - start)

# 간단한 로직에서는 패키지가 없이 구현하는게 조금 더 빠름
# With Counter: 1.3404457569122314
# Without Counter: 1.2261600494384766
# 실행시간: 2581.69ms
# With Counter: 1.5368916988372803
# Without Counter: 1.021822214126587
# 실행시간: 2573.83ms
# With Counter: 1.3869447708129883
# Without Counter: 1.026310682296753
# 실행시간: 2434.22ms
