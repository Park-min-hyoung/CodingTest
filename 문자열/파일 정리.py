# 1. 입력 받을 때 .을 기준으로 split해서 뒤에꺼만 배열에 담기
# 2. 리스트 사전 순으로 정렬
# 3. Counter 라이브러리 사용 해보기
from collections import Counter

n = int(input())
list = []
for _ in range(n):
    list.append(input().split(".")[1])

counter_list = Counter(list)
print(counter_list)
for key in sorted(counter_list):
    print(key, counter_list[key])