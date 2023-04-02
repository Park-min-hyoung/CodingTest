# 1. 순열을 통해 모든 경우의 수 구하기
# 2. 각 경우를 순회하며 방문할 수 있는 던전의 개수 리스트에 저장
# 3. 최대값 출력
# 4. 최소 필요 피로도와 소모 피로도가 같을 수 있음

from itertools import permutations


def solution(k, dungeons):
    dungeons_order = list(permutations(dungeons, len(dungeons)))

    answer = []
    for idx, dungeon in enumerate(dungeons_order):
        rest_fatigue = k
        dungeon_cnt = 0
        for require_fatigue, use_fatigue in dungeon:
            if rest_fatigue >= require_fatigue:
                rest_fatigue -= use_fatigue
                dungeon_cnt += 1
            else:
                break

        answer.append(dungeon_cnt)

    return max(answer)

