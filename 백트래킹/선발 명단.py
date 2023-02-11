# 1. 위의 선수가 선택한 포지션을 제외하고 다 선택해 봄
# 2. 제일 위에 선수가 포지션 1개씩 순회(0이면 pass)
# 3. 제일 위에 선수가 포지션 1개를 선택했을 때 밑에 선수들은 자신의 바로 위의 선수가 선택한 포지션을 제외한 모든 포지션을 돌아 다니기
# => 밑에 선수의 포지션 능력치가 0이면 제외 시켜주기

import copy
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    soccer_position_lst = [list(map(int, input().split())) for _ in range(11)]
    max_ability = 0

    def positioning(men, ability_idx, visited_lst, ability):
        global max_ability

        if not visited_lst[men][ability_idx]:
            visited_lst[men][ability_idx] = True

            for men_idx in range(men + 1, 11):
                visited_lst[men_idx][ability_idx] = True

        if men < 10:
            for next_able_idx, next_able in enumerate(soccer_position_lst[men + 1]):
                if next_able > 0 and not visited_lst[men + 1][next_able_idx]:
                    copy_visited_lst = copy.deepcopy(visited_lst)
                    positioning(men + 1, next_able_idx, copy_visited_lst, ability + next_able)
        else:
            max_ability = max(max_ability, ability)


    for able_idx, able in enumerate(soccer_position_lst[0]):
        visited = [[False] * 11 for _ in range(11)]
        if able > 0: positioning(0, able_idx, visited, able)

    print(max_ability)