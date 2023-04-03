# 0. 사전을 통해 그래프 만들기
# 1. 1번 노드를 제외한 노드가 1번이랑 연결 되는 것 중에 가장 짧은 것(BFS)
# 2. BFS를 통해서 각 노드의 최소 길이 값 리스트 생성
# 3. 최소 길이 값 리스트에서 최대 값을 구한 후 리스트를 순회하며 같은 값이 있다면 결과값 최신화

from collections import defaultdict
from collections import deque


def solution(n, edge):
    graph_dic = defaultdict(list)
    for start, end in edge:
        graph_dic[start].append(end)
        graph_dic[end].append(start)

    queue = deque()
    queue.append([1, 0])
    visited = [True] + [False] * (n - 1)
    length_lst = [0]
    while queue:
        nodes, length = queue.popleft()

        for node in graph_dic[nodes]:
            if not visited[node - 1]:
                visited[node - 1] = True
                queue.append([node, length + 1])
                length_lst.append(length + 1)

    max_edge = max(length_lst)
    answer = 0
    for length in length_lst:
        if max_edge == length: answer += 1

    return answer