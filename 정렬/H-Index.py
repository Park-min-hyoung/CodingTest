def solution(citations):
    result = []
    for idx in range(len(citations) + 1):
        over, down = 0, 0
        for next_idx in range(len(citations)):
            if idx <= citations[next_idx]:
                over += 1
            else:
                down += 1

        if over >= idx and down <= idx:
            result.append(idx)

    if result:
        return max(result)
    else:
        return -1