# 1. DFS 이용

def solution(word):
    current_word = []
    word_lst = []

    def dfs():
        if len(current_word) == 5:
            return

        for idx, w in enumerate(['A', 'E', 'I', 'O', 'U']):
            current_word.append(w)
            word_lst.append(''.join(current_word))

            dfs()
            current_word.pop()

    dfs()

    return word_lst.index(word) + 1