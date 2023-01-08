# 1. 기존 단어와 기존 단어를 뒤집은게 같으면 회문이므로 0 출력
# 2. 유사회문을 알아내는 방법1 => 문자를 하나씩 제거하면서 회문인 것을 판단 => 30 * 10만 * 뒤집는 시간(시간 초과 발생)
# 3. 유사회문을 알아내는 방법2 => 유사회문을 찾을 때 양쪽 끝이 같으면 유사 회문 조건을 가지고 있기 때문에 pass 해도 된다는 생각 => "투 포인터"
# 4. 만약 양쪽 끝이 같지 않다면 그 위치에서 유사회문인지 아닌지 판단(summuus로 설명)
# => "시작점 ~ 끝점 바로 앞 문자열"과 이것을 뒤집은 문자열이 같음(마지막 문자 제거)
# => "시작점 다음 문자 ~ 끝점 문자열"과 이것을 뒤집은 문자열이 같음(처음 문자 제거)
# => 둘중에 하나라도 조건에 부합하면 유사회문, 그렇지 않다면 영원히 유사회문이 될 수 없으므로 일반 문자열

n = int(input())
for _ in range(n):
    check = False
    str = input()

    if str == str[::-1]:
        print(0)
        continue

    start = 0
    end = len(str) - 1
    while start < end:
        if str[start] == str[end]:
            start += 1
            end -= 1
            continue

        if str[start:end] == str[start:end][::-1] or str[start + 1:end + 1] == str[start + 1:end + 1][::-1]:
            print("1")
            check = True
        break

    if not check: print("2")