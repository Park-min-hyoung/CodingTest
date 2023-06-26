# 1. 장르를 key로 하고 paly수 배열을 value로 하는 dict 생성
# 2. [장르, 장르의 총 play수] 배열을 만들거나 사전을 통해 장르명 내림차순
# 3. play수 배열을 내림차순

from collections import defaultdict

def solution(genres, plays):
    album_dic = defaultdict(list)
    play_sum_dic = defaultdict(int)

    for idx, genre in enumerate(genres):
        album_dic[genre].append([idx, plays[idx]])
        play_sum_dic[genre] += plays[idx]

    result = []
    for (genre, price_sum) in sorted(play_sum_dic.items(), key=lambda x:-x[1]):
        for (idx, price) in sorted(album_dic[genre], key=lambda x:-x[1])[:2]:
            result.append(idx)

    return result