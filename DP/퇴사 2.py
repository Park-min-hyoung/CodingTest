# 1. DP
# => 처음 부터 현재 날짜까지 진행을 했을 경우 얻을 수 있는 최대 수입을 담고 있음
# => `목표 날짜에 현재 저장되어 있는 값`과 현재 `목표 날짜까지 상담하는 값`을 비교
# 2. max_value
# => 처음 부터 현재날짜 전까지 진행여부 상관 없이 얻을 수 있는 최대 수입을 나타냄
# => `처음부터 현재날짜 전까지 진행했을 때 얻을 수 있는 최대 수입(max_value)`
# => `다른 날짜(이전)에서 현재날짜로 온 경우 중 최대값(현재 날짜부터 상담 여부 선택, 다른 날짜와 현재 날짜 사이에는 상담 x)`을 비교해 더 큰 값으로 초기화
# 참조 => https://dndi117.tistory.com/entry/aaa

import sys
input = sys.stdin.readline
N = int(input())
period, income = [0], [0]
# 마지막 날 기간이 1인 상담을 진행할 수 있기 때문에 1개 추가 및 숫자 혼동을 위해 1개 추가
DP = [0] * (N + 2)
for _ in range(N):
    p, i = map(int, input().split())
    period.append(p)
    income.append(i)
max_value = 0

for idx in range(N + 1):
    max_value = max(max_value, DP[idx])
    if idx + period[idx] > N + 1:
        continue

    DP[idx + period[idx]] = max(DP[idx + period[idx]], max_value + income[idx])

print(max(DP))
