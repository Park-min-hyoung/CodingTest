import sys
input = sys.stdin.readline

N = int(input())
stone = []

# dp 배열 생성
dp = [1e9] * N
dp[0] = 0
for i in range(N - 1):
    s, b = map(int, input().split())
    stone.append((s, b))
    if i + 1 < N: dp[i+1] = min(dp[i + 1], dp[i] + s)
    if i + 2 < N: dp[i+2] = min(dp[i + 2], dp[i] + b)

# 매우 큰 점프 적용해보며 최솟값 찾기
K = int(input())

_min = dp[-1]
for i in range(3, N):
    e, one_jump, two_jump = dp[i - 3] + K, 1e9, 1e9
    for j in range(i, N-1):
        if i + 1 < N: one_jump = min(one_jump, e + stone[j][0])
        if i + 2 < N: two_jump = min(two_jump, e + stone[j][1])
        e, one_jump, two_jump = one_jump, two_jump, 1e9
    _min = min(_min, e)

print(_min)

# 1. 작은 점프, 큰 점프만 사용해서 각 돌에 도착했을 때 소요되는 최소 에너지 리스트 구하기
# 2. 매우 큰 점프를 허용하는 돌을 한개씩 순회
# 3. 특정 돌에서 최소 에너지를 찾는 작업을 진행