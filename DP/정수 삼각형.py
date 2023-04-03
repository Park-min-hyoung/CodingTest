def solution(triangle):
    dp = [0, [triangle[0][0]]]

    for row_idx, triangle_row in enumerate(triangle[1:], 2):
        new_value_lst = []
        for idx, value in enumerate(triangle_row):
            if idx == 0:
                new_value_lst.append(dp[row_idx - 1][0] + value)
            elif idx == len(triangle_row) - 1:
                new_value_lst.append(dp[row_idx - 1][-1] + value)
            else:
                new_value_lst.append(max(dp[row_idx - 1][idx - 1], dp[row_idx - 1][idx]) + value)

        dp.append(new_value_lst)

    return max(dp[-1])