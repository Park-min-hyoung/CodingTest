from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
distance_map = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

def BFS():
    vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while queue:
        pop_x, pop_y, pop_value = queue.popleft()
        for idx in range(4):
            nx = pop_x + vector[idx][0]
            ny = pop_y + vector[idx][1]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and distance_map[nx][ny] == 1:
                visited[nx][ny] = True
                distance_map[nx][ny] = pop_value + 1
                queue.append([nx, ny, pop_value + 1])


queue = deque([])
for i in range(M):
    for j in range(N):
        if distance_map[i][j] == 2:
            visited[i][j] = True
            distance_map[i][j] = 0
            queue.append([i, j, 0])
            break

BFS()

# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1
for i in range(M):
    for j in range(N):
        if distance_map[i][j] == 1 and not visited[i][j]:
            distance_map[i][j] = -1

for item in distance_map:
    print(*item)