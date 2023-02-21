# 1. 익은 토마토가 있다면 다음날에 익은 토마토가 있는 칸을 기준으로 4방향에 토마토가 익는다.
# 2. 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수
# 3. 입력이 주어졌을 때부터 모든 토마토가 익어있다면 0 출력, 모든 토마토가 익지 못하는 상황이면 -1 출력
# 4. 모든 토마토가 미리 익어있는 상황 check
# => for문을 통해 check
# 5. 모든 토마토가 익지 못하는 상황은 모든 작업을 마무리한 후 0이 한개라도 있으면 -1
# 6. BFS 이용(for문을 통해 순회하면서 queue에다가 1이 있는 곳의 위치를 push), visited, vector, 4방향에 있어 0이면 1로 초기화
# 7. 처음 부터 다 익은 경우, 모든 토마토가 익지 못한 경우, 모든 토마토가 익은 경우
# 8. 모든 토마토가 익은 상태 라면 더 이상 작업을 하지 않아도 됨
'''
1 1 1
0 0 0
1 1 1
'''

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tomato_map = [list(map(int, input().split())) for _ in range(M)]
queue = deque()
visited = [[False] * N for _ in range(M)]


min_distance_lst = []
def BFS():
    vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while queue:
        pop_x, pop_y, pop_value = queue.popleft()
        for idx in range(4):
            nx = pop_x + vector[idx][0]
            ny = pop_y + vector[idx][1]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and tomato_map[nx][ny] == 0:
                visited[nx][ny] = True
                tomato_map[nx][ny] = 1
                queue.append([nx, ny, pop_value + 1])
                min_distance_lst.append(pop_value + 1)


def solution():
    # 처음 입력 받았을 때 익어있는 토마토를 queue에 append(동시에 작업을 해야할 수 있기 때문)
    for i in range(M):
        for j in range(N):
            if tomato_map[i][j] == 1:
                visited[i][j] = True
                queue.append([i, j, 0])

    BFS()

    # 모든 토마토가 익을 수 없는 경우
    for i in range(M):
        for j in range(N):
            if tomato_map[i][j] == 0:
                return -1

    # 처음부터 모든 토마토가 익어있는 경우
    if not min_distance_lst: return 0

    # 모든 토마토가 익는 경우
    return max(min_distance_lst)


result = solution()
print(result)