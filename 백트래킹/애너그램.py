from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    def dfs(length, current_ch):
        if len(str_lst) == length:
            result.append(current_ch)

        for next_ch in ch_number_dic:
            if ch_number_dic[next_ch] > 0:
                ch_number_dic[next_ch] -= 1
                dfs(length + 1, current_ch + next_ch)
                ch_number_dic[next_ch] += 1

    str_lst = list(input().strip())
    ch_number_dic = defaultdict(int)
    for st in str_lst: ch_number_dic[st] += 1
    result = []

    dfs(0, '')

    print('\n'.join(sorted(result)))

# 1. 중복되는 단어를 포함은 시켜야 하지만 그 단어로 탐색은 하지 못하도록 => 리스트 대신 사전을 통한 탐색
# 2. 사전을 이용하기 때문에 중복 된 단어는 탐색을하지 않고 그 단어를 포함할 때는 사전에 있는 그 단어의 개수를 이용하기 때문에 가능
# 3. 이전 소스코드와 비교해 필요없는 자료구조(defaultdict, stack), dfs 내부와 외부의 소스코드 중복, 가지치기를 위한 가지치기
# => defaultdict는 1개로 충분, stack을 사용해도 되지만 현재 진행중인 문자열 dfs의 전달인자로 넘겨줘도 된다.
# => dfs 내부와 외부의 소스코드 중복되는 문제에 있어 이 문제뿐만 아니라 보완을 해야하기 때문에 최대한 호출부에서는 소스코드를 간결하게 해야겠다.
# => 기존의 가지치기를 하기위해서 소스코드를 작성했는데 오히려 가지치기를 하면 시간 복잡도가 줄어들겠지라는 생각만하고 실질적인 시간복잡도를 생각하지 않았다.
# 4. 출처 => https://fre2-dom.tistory.com/468
