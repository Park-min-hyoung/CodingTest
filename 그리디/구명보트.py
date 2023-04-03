# 0. "최대 2명만 탈 수 있음"
# 1. 오름차순 정렬
# 2. 투 포인터 사용해서 오름차순 정렬된 왼쪽 값과 오른쪽 값을 더해서 limit 보다 크다면 boat 카운터 최신화(어차피 오른쪽 값은 최소값을 가진 왼쪽값과 더했을 때 limit가 넘어버리면 어느 값을 넣어주어도 limit보다 크다)

def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1

    boat_cnt = 0
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boat_cnt += 1

    if left == right: boat_cnt += 1
    return boat_cnt