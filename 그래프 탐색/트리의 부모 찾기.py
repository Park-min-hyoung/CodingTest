# 1. 노드 1과 같이 있는 노드들은 visted 처리해주고, index(노드 번호) 설정
# 2. 대응 되는 노드를 저장 후 BFS 사용

import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

N = int(input())
tree_dic = defaultdict(list)
for _ in range(N - 1):
    first, second = map(int, input().split())
    tree_dic[first].append(second)
    tree_dic[second].append(first)

def BFS():
    visited = [True, True] + [False] * (N - 1)
    parent_node_lst = [0] * (N + 1)
    queue = deque([1])

    while queue:
        current_node = queue.popleft()
        for node in tree_dic[current_node]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                parent_node_lst[node] = current_node

    return parent_node_lst

result = BFS()
print("\n".join(map(str, result[2:])))
