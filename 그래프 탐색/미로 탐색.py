# 1. (1, 1)에서 (N, M) 까지의 이동할 때 지내야 하는 최소 칸 수
# 2. 시작 위치와 도착 위치도 포함
# 3. BFS 이용, visited, queue에 다음 수행할 위치랑 현재 까지 지나온 거리 설정
# 4. 메모리 초과 => 방문하고 즉시 방문 check 하지 않으면 잔여 for문(4번)에서 해당 위치를 또 방문할 수 있기에 메모리 초과 발생
# 5. 마지막 위치에 왔다면 queue의 다음 item이 진행되도록 continue

import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    global result_max
    queue = deque()
    queue.append((0, 0, 1))
    visited = [[False] * M for _ in range(N)]

    while queue:
        pop_position_x, pop_position_y, pop_distance = queue.popleft()
        if pop_position_x == N - 1 and pop_position_y == M - 1:
            result_max = max(result_max, pop_distance)
            continue

        for idx in range(4):
            nx = pop_position_x + vector[idx][0]
            ny = pop_position_y + vector[idx][1]
            if 0 <= nx < N and 0 <= ny < M and maze_map[nx][ny] == '1' and not visited[nx][ny]:
                queue.append((nx, ny, pop_distance + 1))
                visited[nx][ny] = True


N, M = map(int, input().split())
maze_map = [list(input().strip()) for _ in range(N)]
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

result_max = 0
BFS()
print(result_max)
