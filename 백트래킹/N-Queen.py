N = int(input())

result = 0
row = [0] * N

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False

    return True

def queen(x):
    global result

    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                queen(x + 1)


queen(0)
print(result)