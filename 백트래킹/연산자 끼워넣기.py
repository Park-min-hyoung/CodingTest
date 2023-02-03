import sys

input = sys.stdin.readline
N = int(input())
numbers_lst = list(map(int, input().split()))
operator_lst = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9

def calc(depth, sum_value, idx):
    if idx == 0: new_sum_value = sum_value + numbers_lst[depth]
    elif idx == 1: new_sum_value = sum_value - numbers_lst[depth]
    elif idx == 2: new_sum_value = sum_value * numbers_lst[depth]
    else: new_sum_value = int(sum_value / numbers_lst[depth])

    operator_lst[idx] -= 1
    dfs(depth + 1, new_sum_value)
    operator_lst[idx] += 1

def dfs(depth, sum_value):
    global max_value, min_value

    if depth == N:
        max_value = max(max_value, sum_value)
        min_value = min(min_value, sum_value)

    if operator_lst[0] > 0: calc(depth, sum_value, 0)
    if operator_lst[1] > 0: calc(depth, sum_value, 1)
    if operator_lst[2] > 0: calc(depth, sum_value, 2)
    if operator_lst[3] > 0: calc(depth, sum_value, 3)


dfs(1, numbers_lst[0])
print(max_value)
print(min_value)