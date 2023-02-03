# 1. 판의 네모들을 하나씩 순회하면서 해당 네모를 포함하지 않거나 포함하는 방법으로 풀이
# 2. 다음 위치를 정할 때 해당 위치가 가장 마지막 열이라면 다음 행에 첫번째로 이동 시키고 그 외에는 오른쪽으로 한칸 이동
# 3. 판의 네모를 포함할 때 현재 네모의 위치의 왼쪽, 위쪽, 좌상단 네모가 하나라도 없어야 2 X 2가 되지 않으므로 포함시킨 후 다음 네모로 이동할 수 있다
# 4. 마지막 다음층의 첫번째 열로 온다면 판을 모두 탐색한 것이므로 count 올려주고 return
# 5. 탐색을 (1, 1) 부터 시작한 이유는 첫번째 행과 첫번째 열의 네모들이 `왼쪽, 위쪽, 좌상단` 탐색할 때 따로 check하지 않아도 됨
# 6. 출처 => https://kjhoon0330.tistory.com/entry/BOJ-14712-%EB%84%B4%EB%AA%A8%EB%84%B4%EB%AA%A8-Python

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
square_map = [[0] * (M + 1) for _ in range(N + 1)]
count = 0

def dfs(x, y):
    global count
    if (x, y) == (N + 1, 1):
        count += 1
        return

    if y == M:
        nx, ny = x + 1, 1
    else:
        nx, ny = x, y + 1

    # 현재 위치를 넣지 않는 경우
    dfs(nx, ny)

    # 현재 위치를 사용하는 경우(다만 현재 위치를 기준으로 왼쪽, 위쪽, 좌상단에 넴모가 하나라도 없어야 가능)
    if square_map[x][y - 1] == 0 or square_map[x - 1][y] == 0 or square_map[x - 1][y - 1] == 0:
        square_map[x][y] = 1
        dfs(nx, ny)
        square_map[x][y] = 0

dfs(1, 1)

print(count)