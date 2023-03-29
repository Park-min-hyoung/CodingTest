def solution(arr):
    stack = [arr[0]]

    for num in arr[1:]:
        if stack[-1] != num:
            stack.append(num)

    return stack