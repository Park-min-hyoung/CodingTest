# 1. 폭탄이 있는 칸은 3초 후에 폭발하고 그 칸을 비롯해 인접한 4칸도 함께 파괴
# => 인접한 칸에 폭탄이 있을 경우 폭발은 하지 않고 파괴만 되기 때문에 연쇄 폭발은 하지 않음
# 2. 1s(가만히 있음), 2s(폭탄이 설치 되지 않은 곳에 설치), 3s(0s 때 설치한 폭탄 폭발),
# => 4s(폭탄이 설치 되지 않은 곳에 설치), 5s(2s 때 설치한 폭탄 폭발)
# 3. 작업
# => 짝수 일때는 그냥 최신화
# => 홀수 일때는 폭발 작업 후에 폭탄 위치 기록
# => queue를 이용해 [현재 폭탄, 미래 폭탄]으로 관리

from collections import deque
import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())
bomb_map = [list(input().strip()) for _ in range(R)]
queue = deque([])
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def plus_bomb():
    bomb_lst = []
    for i in range(R):
        for j in range(C):
            if bomb_map[i][j] == 'O': bomb_lst.append((i, j))
    queue.append(bomb_lst)


for number in range(N + 1):
    if number % 2 == 0:
        if number == 0: plus_bomb()
        else: bomb_map = [['O'] * C for _ in range(R)]
    else:
        if number == 1: continue

        # 폭발 작업
        current_bomb_lst = queue.popleft()
        for x, y in current_bomb_lst:
            bomb_map[x][y] = '.'
            for idx in range(4):
                nx = x + vector[idx][0]
                ny = y + vector[idx][1]
                if 0 <= nx < R and 0 <= ny < C: bomb_map[nx][ny] = '.'

        # 폭탄 추가 작업
        plus_bomb()

for idx in range(R):
    print(''.join(bomb_map[idx]))