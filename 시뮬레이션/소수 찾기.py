def solution(numbers):
    visited = [False] * len(numbers)
    current_str = []
    str_result = []

    def dfs():
        for idx, num_str in enumerate(list(numbers)):
            if not visited[idx]:
                visited[idx] = True
                current_str.append(num_str)
                str_result.append(int(''.join(current_str)))

                dfs()
                visited[idx] = False
                current_str.pop()

    def calc(number):
        if number < 2:
            return False

        for idx in range(2, int(number ** 0.5) + 1):
            if number % idx == 0:
                return False
        return True

    dfs()

    answer = []
    for num in set(str_result):
        if calc(num): answer.append(num)

    return len(answer)