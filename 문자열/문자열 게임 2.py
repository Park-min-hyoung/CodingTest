# 1. 특정 문자 n개가 들어 있는 문자열 => 가장 짧거나 긴 것
# 2. 입력으로 주어진 개수만큼 있는 단어를 사전에 "문자 : index" 형태로 저장(Counter, defaultdict 사용)
# 3. index 리스트를 개수만큼 앞으로 전진 시켜보기?
# 4. 한개 밖에없을 때 틀렸음
# => 리스트의 마지막은 check 하지 않아도 되서 범위를 len(char_idx_lst) - 1로 했음
# => 리스트에 한개의 값이 있을 때는 마지막 값도 길이로 계산 해줘야 하므로 len(char_idx_lst) 수정하니 통과과
from collections import Counter
from collections import defaultdict

n = int(input())
for _ in range(n):
    str = input()
    overlap_number = int(input())

    counter_lst = Counter(str)
    chars_idx_dic = defaultdict(list)
    for idx, s in enumerate(str):
        if counter_lst[s] >= overlap_number:
            chars_idx_dic[s].append(idx)

    result = []
    for char_key in chars_idx_dic:
        char_idx_lst = chars_idx_dic[char_key]
        for char_idx in range(len(char_idx_lst)):
            if char_idx + overlap_number - 1 < len(char_idx_lst):
                result.append(char_idx_lst[char_idx + overlap_number - 1] - char_idx_lst[char_idx] + 1)

    print(min(result), max(result)) if result else print(-1)