# 1. 동전을 이용해 목표 가격이 되도록 하는 경우의 수
# 2. 사용한 동전의 구성이 같은데 순서만 다른 것은 같은 경우
# 3. 값을 기준으로 내림차순 한 후 각 동전을 사용할 수 있는 개수를 리스트로 만들기
# 4. 그 리스트를 기준으로 큰 가치를 가진 동전부터 DFS

import sys
from collections import defaultdict
input = sys.stdin.readline
N, K = map(int, input().split())
coin_lst = [int(input()) for _ in range(N)]
coin_lst.sort(reverse=True)

def dfs(depth, coin_sum):
    global result
    if depth == N - 1:
        if coin_final_dic[K - coin_sum]: result += 1
        return

    for coin in coin_price_lst[depth]:
        dfs(depth + 1, coin_sum + coin)
        if coin_sum + coin + coin_price_lst[depth][1] > K:
            break


result = 0
coin_price_lst = []
for coin_price in coin_lst:
    cnt = K // coin_price
    coin_price_lst.append([x * coin_price for x in range(0, cnt + 1)])
coin_final_value = coin_lst.pop()
coin_final_dic = defaultdict(bool)
for idx in range(0, K + 1, coin_final_value):
    coin_final_dic[idx] = True

dfs(0, 0)

print(result)
