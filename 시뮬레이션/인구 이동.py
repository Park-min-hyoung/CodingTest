# 1. 국경선을 어떻게 설정할 지 고민(DFS), 국경선 visit 배열(0, 1), 연합에 속한 나라 position 배열(평균 계산 및, 국가 값 초기화)
# => 처음에는 국가들을 한번씩 돌며 4방향을 고려 해보는 방식으로 풀이
# => 해설을 통해 하루 동안 서로 연합 될 국가를 찾기 위해 BFS를 이용했는데 DFS도 될 것 같아 시도
# 2. 하나의 국가를 방문하면서 인접한 국가와의 인구차이 조건을 만족하면 지금 방문한 국가와 인접한 국가를 1을 통해 방문 표시
# => 탐색을 시작한 지점(연합 국가를 찾기 위한 시작 국가)에서는 방문과 동시에 1로 수정 => 연합 국가가 없다고 해서 1로 수정하지 않는다면 다른 곳에서 이 국가를 또 방문
# 3. 가지치기를 할 때 인접한 국가가 1이면 pass(0이여만 진행), 다만 내가 1일 때는 다른 국가와 인접 여부 check를 위해 진행
# => BFS를 통해 방문한 국가와 방문하지 않은 국가를 구별할 수 있기 때문에 추가적인 설명은 필요없고 간결하게 표현 가능
# 4. 방문한 곳의 위치를 배열에 넣어두기
# => 외부에 배열을 선언한 다음에 사용 => BFS가 시작되는 점에서 선언 및 BFS 시작점을 넣어주고 작업이 끝난 후 return
# => 처음 방법도 나쁘지는 않은데 작업이 끝날 때 마다 다시 빈 배열로 초기화 해야하는 번거로움이 있고 return 값을 통해 이 함수가 개인적으로는 명확해 가독성이 높음
# 5. 방문한 곳의 위치 배열을 통해 기존의 국가 인구를 최신화 했다면 위치 배열과 방문 check 여부 배열(0과 1) 최신화
# => visited의 경우도 외부에서 선언 및 초기화 했는데 `하루`가 시작 될 때(while True 시작 부분) 방문을 초기화 하면 나중에 초기화 하지 않아도 됨
# => 인구 최신화에 필요한 avg 값을 구하기 위해 sum 관련 배열을 선언 했었는데 `리스트 컴프리헨션`을 통해 연합 국가의 총합을 구할 수 있었음
# 6. 연합 된 국가의 인구 수를 최신화 할 때 마다 result가 올라간다고 잘못 생각함
# => 원래 문제보다 더 어렵게 이해, 그냥 이중 for문(하루를 보낼 때)을 돌 때 연합이 있었다면 result에 +1 해주고 없었다면 작업 중지
# 7. 배운점 => import sys를 통해 만든 input, 자료구조를 무조건 외부에 사용하기 보다는 적절한 곳에 사용하게 되면 필요없는 소스코드를 작성하지 않아도 된다, 리스트 컴프리헨션

from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
country_map = [list(map(int, input().split())) for _ in range(N)]
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]
queue = deque()

def bfs(x, y):
    queue.append([x, y])
    country_position_lst = []
    country_position_lst.append([x, y])

    while queue:
        pop_x, pop_y = queue.popleft()
        for idx in range(4):
            nx = pop_x + vector[idx][0]
            ny = pop_y + vector[idx][1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                difference_value = abs(country_map[nx][ny] - country_map[pop_x][pop_y])
                if L <= difference_value <= R:
                    visited[nx][ny] = 1
                    country_position_lst.append([nx, ny])
                    queue.append([nx, ny])

    return country_position_lst


result = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs_position_lst = bfs(i, j)
                # 한 국가라도 연합이 되었다면
                if len(bfs_position_lst) > 1:
                    flag = 1
                    move_avg_number = sum(list(country_map[x][y] for x, y in bfs_position_lst)) // len(bfs_position_lst)
                    for x, y in bfs_position_lst:
                        country_map[x][y] = move_avg_number

    if not flag: break
    result += 1

print(result)