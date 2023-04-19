# 1. 약수 개수 구하는 함수 만들기
# 2. 개수가 짝수면 더해주고 홀수면 빼기

import math


def solution(left, right):
    def calc(num):
        result = []
        for n in range(1, int(math.sqrt(num)) + 1):
            if num % n == 0:
                result.append(n)
                result.append(num // n)

        return len(set(result))

    number_sum = 0
    for number in range(left, right + 1):
        if calc(number) % 2 == 0:
            number_sum += number
        else:
            number_sum -= number

    return number_sum