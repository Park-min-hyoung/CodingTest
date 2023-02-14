# 1. 12명 이면 111명 까지 검사(C + 100) => C명에 대한 최소 비용을 출력할 때, C명 보다 많은 고객 수에서 최소 비용이 나올 수 있음
# 2. 100명을 더 추가한 이유는
# 3. 8명을 구하려고 할 때, 3원에 5명 모집 조건을 수행
# => `과거의 구해 둔 8명 모집 최소 비용`과 `현재 8명 모집 최소 비용`중 작은 값
# 참조 => https://bio-info.tistory.com/218

import sys
input = sys.stdin.readline
require_promotion_men, city = map(int, input().split())
city_lst = [list(map(int, input().split())) for _ in range(city)]
DP = [1e7] * (require_promotion_men + 100)
DP[0] = 0

for cost, promotion_men in city_lst:
    for current_promotion_men in range(promotion_men, require_promotion_men + 100):
        DP[current_promotion_men] = min(DP[current_promotion_men], DP[current_promotion_men - promotion_men] + cost)

print(min(DP[require_promotion_men:]))