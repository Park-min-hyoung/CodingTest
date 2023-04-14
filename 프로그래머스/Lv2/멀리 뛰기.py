def solution(n):
    dp = [0, 1, 2, 3] + [0] * (n - 3)

    for idx in range(4, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

    return dp[n] % 1234567