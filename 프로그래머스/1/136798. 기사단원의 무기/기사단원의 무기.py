def solution(number, limit, power):
    def count_divisors(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count

    total_weight = 0
    for i in range(1, number + 1):
        attack = count_divisors(i)
        if attack > limit:
            total_weight += power
        else:
            total_weight += attack

    return total_weight