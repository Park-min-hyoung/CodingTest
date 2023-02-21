# # 1. 무조건 바이러스를 먼저 막는게 좋은 방법일까?
# # 2. 바이러스가 퍼지지 않도록 하는 방법이 있고 바이러스는 퍼지도록 나두고 안전지대만 만드는 경우도 있음
# # 3. 첫번째는 밑에서 세번째 줄까지, 두번째는 첫번째 for문의 시작점에서 밑에서 두번쨰 줄까지, 세번째는 두번째 for문의 시작에서 끝까지
# # 4. 벽을 세운 작업 후에 BFS 돌고 0의 개수 계산하기

from collections import deque
import copy
import sys
input = sys.stdin.readline


max_value = 0
def bfs():
    vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    copy_laboratory_map = copy.deepcopy(laboratory_map)
    copy_queue = copy.deepcopy(queue)

    while copy_queue:
        pop_x, pop_y = copy_queue.popleft()
        for idx in range(4):
            nx = pop_x + vector[idx][0]
            ny = pop_y + vector[idx][1]
            if 0 <= nx < M and 0 <= ny < N and copy_laboratory_map[nx][ny] == 0:
                copy_laboratory_map[nx][ny] = 2
                copy_queue.append([nx, ny])

    global max_value
    value = 0
    for item in copy_laboratory_map:
        value += item.count(0)

    max_value = max(value, max_value)


def build_wall(current_cnt):
    if current_cnt == 3:
        bfs()
        return

    for row in range(M):
        for col in range(N):
            if laboratory_map[row][col] == 0:
                laboratory_map[row][col] = 1
                build_wall(current_cnt + 1)
                laboratory_map[row][col] = 0


M, N = map(int, input().split())
laboratory_map = [list(map(int, input().split())) for _ in range(M)]
queue = deque([])

for i in range(M):
    for j in range(N):
        if laboratory_map[i][j] == 2:
            queue.append([i, j])

build_wall(0)
print(max_value)
