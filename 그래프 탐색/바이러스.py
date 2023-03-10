# 1. 특정 컴퓨터에 바이러스가 걸리면 특정 컴퓨터와 연결되어있는 컴퓨터들은 모두 감염
# 2. 1번 컴퓨터가 바이러스가 걸린 상황
# 3. 특정 컴퓨터에 연결되어있는 컴퓨터를 나타내는 사전(특정 컴퓨터보다 숫자가 큰 컴퓨터만 check)
# 4. 3번 괄호 내용을 토대로 소스코드를 작성했지만 문제 발생(3번과 7번이 연결되었을 경우 4 > 7 경로만 설정했다면 전파가 되지 않음)

import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

N = int(input())
line = int(input())
computer_line_dic = defaultdict(list)
for _ in range(line):
    start, end = map(int, input().split())
    computer_line_dic[start].append(end)
    computer_line_dic[end].append(start)

visited = [False, True] + [False] * (N - 1)
queue = deque([1])
result = 0
while queue:
    pop_position = queue.popleft()

    for next_position in computer_line_dic[pop_position]:
        if not visited[next_position]:
            result += 1
            queue.append(next_position)
            visited[next_position] = True

print(result)