# 1. priorities 리스트 값에 현재 시작 위치, 우선순위 설정
# 2. 현재 출력되야 할 우선순위라면
# => location이 같으면 break 및 count return
# => location이 다르면 출력하고 작업 유지, 진행되어야 할 우선순위 최신화, count 최신화
# 3. 현재 출력되야 할 우선순위가 아니라면 현재 아이템을 뒤로

from collections import deque
from collections import defaultdict


def solution(priorities, location):
    priority_dic = defaultdict(int)
    for priority in priorities:
        priority_dic[priority] += 1
    priority_dic_keys = sorted(list(priority_dic))

    priorities_idx_lst = deque([])
    for idx in range(len(priorities)):
        priorities_idx_lst.append([priorities[idx], idx])

    print_count = 0
    while priorities_idx_lst:
        if priorities_idx_lst[0][0] < priority_dic_keys[-1]:
            priorities_idx_lst.append(priorities_idx_lst.popleft())
        else:
            # 출력 및 카운터 최신화
            first_position_priority = priorities_idx_lst.popleft()
            print_count += 1

            # 사전을 통해 다음에 출력되어야 할 우선순위 선정
            priority_dic[priority_dic_keys[-1]] -= 1
            if priority_dic[priority_dic_keys[-1]] == 0:
                priority_dic_keys.pop()

            # 내가 원하는 출력물이라면 프로그램 종료
            if first_position_priority[1] == location:
                break

    return print_count