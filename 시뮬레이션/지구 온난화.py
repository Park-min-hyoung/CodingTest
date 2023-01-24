# 1. 바다인지 섬인지 위치 저장 및 값을 저장할 새로운 배열 생성(deepcopy 이용)
# 2. 반복문 순회하면서 섬일 때(x) 동서남북 확인해서 바다이거나 지도 밖일 경우 counter를 올리고 counter가 3이상이면 바다(.)로 값 수정
# 3. 반복문 순회할 때
# => 처음 row는 설정 후 고정, 마지막 row는 해당 층의 작업이 끝나면 최신화
# => 시작 col 같은 경우 이전 시작 col 값보다 작으면 최신화, 마지막 col 같은 경우 이전 마지막 col 값보다 크면 최신화
# 4. 예외사항(밑에)
# => #1, #2, #3 모두 first_row가 바뀌지 않았을 때, 즉 지도에 있어서 섬이 될 만한 아이템이 하나도 없는 상황이고 섬이 될만한 아이템이 없으니 first_row가 수정되지 않았음
# => after_map의 결과를 보게되면 모든 아이템이 바다로 표시 된 것을 볼 수 있지만 문제에서 섬이 1개는 있어야 한다고 했으므로 이 경우에는 X 출력

import copy

R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]
after_map = copy.deepcopy(map)
vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]
first_row, final_row, first_col, final_col = -1, 0, C - 1, 0

def vetor_check(x, y):
    counter = 0
    for i in range(4):
        nx = x + vector[i][0]
        ny = y + vector[i][1]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or map[nx][ny] == '.':
            counter += 1

    return '.' if counter >= 3 else 'X'


for r in range(R):
    for c in range(C):
        if map[r][c] == 'X':
            after_map[r][c] = vetor_check(r, c)
            # first_row를 0으로 설정하게 되면 1층에 섬이 있을 때 first_row는 0으로만 초기화
            # 2층으로 내려갔을 때 이미 1층에서 check가 완료되었으므로 check하면 안되는데 first_row가 0이기 때문에 check 하는 문제 발생
            if first_row == -1 and after_map[r][c] == 'X': first_row = r
            if c < first_col and after_map[r][c] == 'X': first_col = c
            if after_map[r][c] == 'X': final_row = r
            if c > final_col and after_map[r][c] == 'X': final_col = c

result = []
for row in range(first_row, final_row + 1):
    result.append("".join(after_map[row][first_col:final_col + 1]))
print('X') if first_row == -1 else print("\n".join(result))

'''
#1
1 1
X

#2
2 1
X
X

#3
5 3
...
...
.X.
...
...
'''