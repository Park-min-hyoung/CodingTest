def solution(numbers, target):
    result = 0

    def dfs(num, idx, numbers_sum):
        numbers_sum += num
        if idx == len(numbers) - 1:
            if numbers_sum == target:
                result += 1
            return
        # 양수
        dfs(numbers[idx + 1], idx + 1, numbers_sum)
        # 음수
        dfs(-numbers[idx + 1], idx + 1, numbers_sum)

    result = []
    dfs(0, -1, 0)

    return sum(result)