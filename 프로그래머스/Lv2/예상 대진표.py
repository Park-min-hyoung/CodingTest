# 1. 홀수면 더하기 1해서 나누기 2, 짝수면 그냥 나누기 2
# 2. 입력으로 주어진 두 값의 차이의 절대값이 1이면 종료

def solution(n, a, b):
    round_cnt = 1

    while True:
        if abs(a - b) == 1 and max(a, b) % 2 == 0:
            return round_cnt

        round_cnt += 1

        if a % 2 == 0:
            a //= 2
        else:
            a = (a + 1) // 2

        if b % 2 == 0:
            b //= 2
        else:
            b = (b + 1) // 2