# 문제 파악
# => 처음에는 빈틀, 후보를 추천하면 사진틀에 사진 박제
# => 비어있는 사진틀이 없다면 추천수가 가장 작은 사진 때어내고 붙이기, 만약 가장 작은 추천수를 가진 후보가 2명이면 추천을 한지 오래된 후보 사진 제거
# => 만약 사진틀에 있는 후보를 추천하였을 경우 사진 박제 작업은 하지 않고 추천수만 올리기, 사진이 삭제되는 경우 추천수는 0으로 초기화
# 문제 풀이 생각
# 1. 우선 순위 큐(추천수가 제일 적은 후보가 가장 앞으로, 제일 적은 후보가 2명 이상일 때는 들어온 순서)
# 2. 순서를 보장(가장 적은애, 가장 적은애가 둘이 있을때는 가장 처음에 들어온 애 => 가장 처음에 들어왔지만 나보다 작은애가 있다면 그 애가 나가야 함)
# 3. defaultdict, queue, 최소값 정해놓기

from collections import defaultdict
from collections import deque

picture = int(input())
vote = int(input())
vote_lst = map(int, input().split())
vote_queue = deque([])
current_vote_dic = defaultdict(int)

for idx, v in enumerate(vote_lst):
    current_vote_dic[v] += 1
    # 액자에 자리가 없고 액자에 등록되지 않은 새로운 후보라면
    if len(vote_queue) == picture and current_vote_dic[v] == 1:
        sort_vote_dic = sorted(list(current_vote_dic.items())[:-1], key=lambda x: x[1])
        dict_min_key = sort_vote_dic[0][0]

        del current_vote_dic[dict_min_key]
        vote_queue.remove(dict_min_key)

    if current_vote_dic[v] == 1: vote_queue.append(v)

print(*sorted(vote_queue))

'''
#1. 모두 같은 경우
3
7
2 2 3 3 4 4 5
=> 3 4 5

#2. 1이 제거되는 것이 아니라 3이 제거 되어야 함
3
10
1 1 1 1 2 2 2 3 3 4
=> 1 2 4

'''