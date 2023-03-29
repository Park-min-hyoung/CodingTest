# 1. '('로 열렸으면 ')'로 반드시 닫혀야 한다.
# 2. stack에 아무것도 없을 때 ')'가 들어올 차례면 올바른 괄호가 아님

def solution(s):
    answer = True
    stack = []

    for bracket in s:
        if bracket == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break

    if stack: answer = False
    return answer