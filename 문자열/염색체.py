n = int(input())

def calc(idx, first, second):
    if chr[idx] != first and chr[idx] != second:
        return "Not Pattern"
    if chr[idx] == first:
        return first
    if chr[idx] == second:
        return second


for idx in range(n):
    chr = input()
    a_postion = chr.find('A')
    target_keyword = 'A'

    if a_postion >= 2 or a_postion == -1:
        print('Good')
        continue

    if a_postion == 1 and chr[0] not in ['A', 'B', 'C', 'D', 'E']:
        print('Good')
        continue

    if chr[-2] == 'C' and chr[-1] not in ['A', 'B', 'C', 'D', 'E']:
        print('Good')
        continue

    for idx in range(a_postion + 1, len(chr)):
        if target_keyword == 'A':
            target_keyword = calc(idx, 'A', 'F')

        elif target_keyword == 'F':
            target_keyword = calc(idx, 'F', 'C')

        elif target_keyword == 'C':
            target_keyword = calc(idx, 'C', 'C')

        if target_keyword == "Not Pattern":
            break

    print("Good") if target_keyword == "Not Pattern" else print('Infected!')