# 1. Counter 사용해서 특정 숫자가 몇개 있는지 파악
# 2. [특정 숫자, 특정 숫자의 개수]를 원소로 가지고 있는 이중 배열 선언
# 3. 이중 배열을 특정 숫자의 개수가 많은 순으로 정렬
# 4. 이중 배열을 순회하며 특정 숫자의 개수를 더하는 작업을 진행, 누적값이 k보다 크면 break

from collections import Counter

def solution(k, tangerine):
    number_dic = Counter(tangerine)
    tangerine_lst = []
    for number in set(tangerine):
        tangerine_lst.append([number, number_dic[number]])

    tangerine_lst.sort(key=lambda x: x[1], reverse=True)

    current_number = 0
    number_cnt = 0
    for number, cnt in tangerine_lst:
        number_cnt += 1
        current_number += cnt

        if current_number >= k: break

    return number_cnt