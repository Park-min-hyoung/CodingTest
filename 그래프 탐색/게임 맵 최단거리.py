# 1. 최단 거리는 bfs 이용
# 2. 방문한 곳을 또 방문할 수 있으므로 visited 배열 설정
# 3, 적의 위치에 방문했을 때 return, 방문할 수 있는 곳에 모두 방문했음에도 적의 위치에 가지 못하는 경우에는 -1 return

from collections import deque


def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    queue = deque([[0, 0, 1]])
    while queue:
        pop_x, pop_y, visited_cnt = queue.popleft()

        for idx in range(4):
            nx = pop_x + vector[idx][0]
            ny = pop_y + vector[idx][1]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] == 1:
                # 적의 위치에 방문했다면
                if nx == len(maps) - 1 and ny == len(maps[0]) - 1:
                    return visited_cnt + 1

                visited[nx][ny] = True
                queue.append([nx, ny, visited_cnt + 1])

    return -1