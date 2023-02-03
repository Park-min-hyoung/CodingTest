# 1. 출발점이 어떤 도시 든 될 수 있으므로 모든 도시에서 출발하도록 설정
# 2. 시간 복잡도 => 도시의 개수(최대 10) * 특정 도시 탐색 횟수(도시가 10개일때 9!) => 360만 정도
# => 예시에서는 4 * 3! = 24
# 3. 현재 도시에서 다음 도시 이동 시 `가치치기`
# => `길이 없거나(값이 0)`
# => `이미 방문한 도시(단 시작 도시를 제외한 모든 도시의 방문을 마치고 시작 도시로 오는 경우 제외, 방문 카운터로 계산)`일 경우`
# 4. 탐색에 있어 DFS 이용
# 5. 도시 방문 할 때 마다 stack 에다가 방문 도시 넣어주고 다시 돌아올 때 pop해서 도시 제거 함으로써 중복 check 가능
# min_value에 방문할 때 마다 값 넣어주고 모든 방문을 마무리 했을 때 그 값을 모두 더해서 다시 min_value에 넣어주기
# 24개의 길을 기준으로 했을 때 항상 24개의 길을 이용할 수는 없다.

import sys
input = sys.stdin.readline

N = int(input())
load_map = [list(map(int, input().split())) for _ in range(N)]

def dfs():
    if result_min_value and stack and (N + 1 - len(stack)) * min_value + stack[-1][1] >= min(result_min_value):
        return

    if len(stack) == N:
        first_position = stack[0][0]
        final_position = stack[-1][0]
        if load_map[final_position][first_position] != 0:
            final_value = stack[-1][1]
            value = final_value + load_map[final_position][first_position]
            result_min_value.append(value)
        return

    for idx in range(N):
        if not visited[idx]:
            # 한 곳도 방문하지 않았을 경우
            if not stack:
                stack.append([idx, 0])
            else:
                prev_position = stack[-1][0]
                if load_map[prev_position][idx] == 0:
                    continue
                else:
                    prev_value = stack[-1][1]
                    value = prev_value + load_map[prev_position][idx]
                    stack.append([idx, value])
            visited[idx] = True
            dfs()
            stack.pop()
            visited[idx] = False

visited = [False] * N
stack = []
min_value = 1000000
for i in range(N):
    for j in range(N):
        if load_map[i][j] != 0: min_value = min(load_map[i][j], min_value)
result_min_value = []

dfs()

print(min(result_min_value))

# 1. visited를 통해 방문 check, stack을 통해 이동했던 내역을 저장
# 2. 지금 구한 값들의 최소값보다 현재 진행되고 있는 값 + 진행 횟수 * board의 최소값이 크다면 retrun
# => 최소값이 아닐지라도 최소값을 넣어주었는데도 구한 값들보다 크다면 가망이 없으므로 가지치기
# 3. 이전의 필요없는 소스코드(특정 도시에 대응하는 도시 저장(defaultdict), dfs 안쪽이랑 바깥쪽에 중복되는 소스코드)와 최소값을 통한 가지치기가 수정