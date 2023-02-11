N = int(input())

dp = [0, '1', '12', '121']

for idx in range(4, N + 1):
    if dp[idx - 1][-1] == '1':
        if dp[idx - 1][-3:-1] != dp[idx - 1][-1] + '2':
            dp.append(dp[-1] + '2')
        else:
            dp.append(dp[-1] + '3')

    elif dp[idx - 1][-1] == '2':
        if dp[idx - 1][-3:-1] != dp[idx - 1][-1] + '1':
            dp.append(dp[-1] + '1')
        else:
            dp.append(dp[-1] + '3')

    else:
        if dp[idx - 1][-3:-1] != dp[idx - 1][-1] + '1':
            dp.append(dp[-1] + '1')
        else:
            dp.append(dp[-1] + '2')

if N >= 4: print(dp[-1])
else: print(dp[N])