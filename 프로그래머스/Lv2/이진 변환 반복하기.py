# 1. 0제거 => 0 제거한 문자열의 길이 값을 2진수로 변환
# 2. 1번 작업 시에 2진수로 변환했을 때 1만 남으면 변환 횟수와 0이 사라진 개수 반환

def solution(s):
    remove_zero_cnt = 0
    format_cnt = 0
    current_s = s
    while True:
        format_cnt += 1

        current_s = "".join(s.split('0'))
        remove_zero_cnt += (len(s) - len(current_s))
        s = format(len(current_s), 'b')

        if s == '1':
            return [format_cnt, remove_zero_cnt]