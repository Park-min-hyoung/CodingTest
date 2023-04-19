# 1. 연결을 한개씩 끊기
# 2. dfs를 통해 1번부터 끊어질때 까지 탐색 한 다음 나온 개수와 나머지 개수를 구하기

from collections import defaultdict


def solution(n, wires):
    def dfs(next_number, graph_dic, visited, cnt_count):
        for num in graph_dic[next_number]:
            if not visited[num]:
                visited[num] = True
                cnt_count.append(1)
                dfs(num, graph_dic, visited, cnt_count)

        return len(cnt_count)

    result = []
    for idx in range(len(wires)):
        remove_wires = wires[:idx] + wires[idx + 1:]
        graph_dic = defaultdict(list)
        for start, end in remove_wires:
            graph_dic[start].append(end)
            graph_dic[end].append(start)

        visited = [True, True] + [False] * (n - 1)
        dfs_node_cnt = dfs(1, graph_dic, visited, [1])

        result.append(abs(dfs_node_cnt - (n - dfs_node_cnt)))

    return min(result)