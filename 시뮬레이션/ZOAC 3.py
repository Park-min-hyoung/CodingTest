# 1. 사전을 통해 자음과 모음의 위치 설정
# 2. 처음 입력으로 주어진 문자가 각각 자음과 모음이므로 자음과 모음의 위치 리스트를 생성
# 3. 문자열을 순회하며 문자의 자음, 모음 여부 check 해서 `조건에 일치하는 리스트`의 `마지막 위치값`과 `현재 위치값`을 계산해서 시간 증가 시키기
# 4. 시간을 증가시킨 후에는 특정 리스트에 새로운 위치 append

constant_dic = {'q': [0, 0], 'w': [0, 1], 'e': [0, 2], 'r': [0, 3], 't': [0, 4],
                'a': [1, 0], 's': [1, 1], 'd': [1, 2], 'f': [1, 3], 'g': [1, 4],
                'z': [2, 0], 'x': [2, 1], 'c': [2, 2], 'v': [2, 3]}
vowel_dic = {'y': [0, 5], 'u': [0, 6], 'i': [0, 7], 'o': [0, 8], 'p': [0, 9],
             'h': [1, 5], 'j': [1, 6], 'k': [1, 7], 'l': [1, 8],
             'b': [2, 4], 'n': [2, 5], 'm': [2, 6]}

left_ch, right_ch = input().split(" ")
goal_str = input()

left_finger_lst = [constant_dic[left_ch]]
right_finger_lst = [vowel_dic[right_ch]]

def process(target_lst, target_dic):
    prev_final_idx_lst = target_lst[-1]
    current_idx_lst = target_dic[ch]
    target_lst.append(current_idx_lst)
    return abs(prev_final_idx_lst[0] - current_idx_lst[0]) + abs(prev_final_idx_lst[1] - current_idx_lst[1]) + 1

result = 0
for ch in goal_str:
    if ch in constant_dic: result += process(left_finger_lst, constant_dic)
    else: result += process(right_finger_lst, vowel_dic)

print(result)