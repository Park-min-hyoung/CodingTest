# 1. 시작점 설정(처음에는 0) => 태그가 열린 경우, 태그가 닫힐 경우, 태그가 아닐 때 공백이 들어온 경우(수정해보기)
# 2. 데이터가 들어가는 경우
# => 태그가 열리는 경우(시작점 ~ 태그 열리기 전 idx)
# => 태그가 닫힐 때(시작점(태그가 열리는 idx ~ 태그의 끝 idx)
# => 태그 안이 아닐 때 공백일 경우(시작점 ~ 공백 전 idx + 공백)
# 3. 마지막 문자가 출력 안됨 => 마지막 태그 뒤 혹은 마지막 공백 뒤 문자가 있는 경우 출력 x => 출력전 마지막 문자열 추가

str = input()
stack = []
lst = []
start = 0
for idx, st in enumerate(str):
    if st == '<':
        if start < idx: lst.append(str[start:idx][::-1])
        stack.append('<')
        start = idx
    elif st == '>':
        lst.append(str[start:idx + 1])
        stack.pop()
        start = idx + 1
    elif st == " ":
        if stack: continue
        lst.append(str[start:idx][::-1] + " ")
        start = idx + 1

lst.append(str[start:][::-1])
print("".join(lst))