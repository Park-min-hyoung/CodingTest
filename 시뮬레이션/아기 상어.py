# 1. 아기 상어의 위치 값과 초기 값 설정
# 2. 고래가 먹이를 찾으로 다닐 때(BFS 한번) queue(다음 방문할 곳 저장), visited, distance, eat_fish_lst(먹은 물고기의 위치와 시작점과의 거리)를 초기화
# 3. 자신 보다 크기가 같거나 작은 물고기가 있는 곳에 갈 수 있다. 다만 0을 제외한 자신보다 size가 작은 물고기만 먹을 수 있음
# 4. 먹을 수 있는 물고기가 여러개 있을 때
# => `거리가 가까운게` 여러개 있다면 `제일 위에 물고기`, 제일 위에 물고기가 여러개 있다면 `제일 왼쪽 물고기`
# 5. 아기 상어의 출발점과 먹은 물고기가 있는 곳을 0으로 수정하고 아기상어의 위치를 먹은 물고기 위치로 수정
# 6. 아기상어 level up 조건 및 조건이 충족 되면 level up 시키기

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
fish_map = [list(map(int, input().split())) for _ in range(N)]
x, y, shark_size = 0, 0, 2
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(N):
    for j in range(N):
        if fish_map[i][j] == 9:
            x = i
            y = j

def bfs(x, y, size):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    queue = deque([[x, y]])
    distance_lst = [[0] * N for _ in range(N)]
    eat_fish_lst = []

    while queue:
        pop_x, pop_y = queue.popleft()
        for idx in range(4):
            nx = pop_x + vector[idx][0]
            ny = pop_y + vector[idx][1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if size >= fish_map[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    distance_lst[nx][ny] = distance_lst[pop_x][pop_y] + 1
                    if size > fish_map[nx][ny] and fish_map[nx][ny] != 0:
                        eat_fish_lst.append([nx, ny, distance_lst[nx][ny]])

    return sorted(eat_fish_lst, key=lambda x:(-x[2], -x[0], -x[1]))


result = 0
cnt = 0
while 1:
    eat_result_lst = bfs(x, y, shark_size)

    if len(eat_result_lst) == 0: break

    result_x, result_y, result_distance = eat_result_lst.pop()
    result += result_distance

    fish_map[x][y], fish_map[result_x][result_y] = 0, 0
    x, y = result_x, result_y

    cnt += 1
    if shark_size == cnt:
        shark_size += 1
        cnt = 0

print(result)