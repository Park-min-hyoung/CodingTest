def solution(n, left, right):
    result = []
    for number in range(left, right + 1):
        row = number // n + 1
        col = number % n + 1

        if row >= col: result.append(row)
        else: result.append(col)

    return result