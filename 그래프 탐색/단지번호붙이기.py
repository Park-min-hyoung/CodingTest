# 1. DFS 이용, visted, 단지 cnt, 단지 별 집 cnt

import sys
input = sys.stdin.readline

def dfs(x, y):
    global group_house_cnt

    for idx in range(4):
        nx = x + vector[idx][0]
        ny = y + vector[idx][1]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and apt_map[nx][ny] == '1':
            visited[nx][ny] = True
            group_house_cnt += 1
            dfs(nx, ny)


N = int(input())
apt_map = [list(input().strip()) for _ in range(N)]
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]
group_cnt = 0
visited = [[False] * N for _ in range(N)]

group_house_cnt_lst = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and apt_map[i][j] == '1':
            group_cnt += 1
            group_house_cnt = 1
            visited[i][j] = True

            dfs(i, j)
            group_house_cnt_lst.append(group_house_cnt)

print(group_cnt)
print('\n'.join(map(str, sorted(group_house_cnt_lst))))