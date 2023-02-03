def dfs(x, y, sum):
    global answer

    if y == M:
        x, y = x + 1, 0
    nx, ny = x, y + 1

    if x == N:
      answer = max(answer, sum)
      return

    if not visited[x][y]:
        for key in range(4):
            first_x, first_y, second_x, second_y = shape[key]
            first_shift_x, first_shift_y, second_shift_x, second_shift_y = \
                x + first_x, y + first_y, x + second_x, y + second_y

            if 0 <= first_shift_x < N and 0 <= second_shift_x < N and \
                    0 <= first_shift_y < M and 0 <= second_shift_y < M and \
                    not visited[first_shift_x][first_shift_y] and not visited[second_shift_x][second_shift_y]:
                visited[x][y] = visited[first_shift_x][first_shift_y] = visited[second_shift_x][second_shift_y] = True
                dfs(nx,
                    ny,
                    sum + board[x][y] * 2 + board[first_shift_x][first_shift_y] + board[second_shift_x][second_shift_y])
                visited[x][y] = visited[first_shift_x][first_shift_y] = visited[second_shift_x][second_shift_y] = False

    dfs(nx, ny, sum)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
shape = {0: [0, -1, 1, 0], 1: [-1, 0, 0, -1], 2: [-1, 0, 0, 1], 3: [0, 1, 1, 0]}
visited = [[False] * M for _ in range(N)]
answer = 0
dfs(0, 0, 0)
print(answer)

# 1. 현재 위치가 방문한 위치가 아니라면 방문해서 4가지 모양이 되는지 시도
# 2. 만약 모양이 만들어지면 현재 부메랑의 총합과 함께 다음 위치(오른쪽 이동, 단, 현재 위치가 마지막 열일 떄는 아래 층의 가장 왼쪽 열로 이동)이동 해서 탐색
# 3. 다음 위치가 방문한 위치라면 다음 위치로 이동하고 방문하지 않았다면 1번 작업을 시작
# 4. 탐색을 하다 마지막 다음 층으로 왔을 경우 탐색이 끝났으므로 총합을 기존의 총합과 비교해 더 크다면 최신화
# 5. 출처 => https://comdolidol-i.tistory.com/313