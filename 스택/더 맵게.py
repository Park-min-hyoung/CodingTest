# 1. heap을 사용해서 첫 번째 원소(최소값)가 K 보다 작으면 작업 진행
# 2. 크면 작업 종료 후 횟수 반환

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    result_cnt = 0
    while len(scoville) >= 2 and scoville[0] < K:
        mix_value = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix_value)

        result_cnt += 1

    if len(scoville) == 1:
        if scoville[0] >= K: return result_cnt
        else: return -1
    return result_cnt
