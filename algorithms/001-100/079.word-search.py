# 单词搜索，20190113
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 人家的解法，自己还不很熟练
        """
        回溯法解决问题，对于word='ABCCED'。从第一个元素开始匹配，然后向后面寻找。
        先统计word 和board 是否有包含关系，如果没有返回False。
        访问过结点使用临时的tmp。我们将board[i][j]="#"。
        """
        def dfs(x, y, word):
            if len(word) == 0:
                return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = "#"
                if dfs(x - 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # down
            if x < len(board) - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = "#"
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = "#"
                if dfs(x, y - 1, word[1:]):
                    return True
                board[x][y] = tmp
            # right
            if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = "#"
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if(dfs(i, j, word[1:])):
                        return True
        return False

        # 人家的解法
    #     visited = [[False for j in range(len(board[0]))]
    #                for i in range(len(board))]

    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if self.existRecu(board, word, 0, i, j, visited):
    #                 return True

    #     return False

    # def existRecu(self, board, word, cur, i, j, visited):
    #     if cur == len(word):
    #         return True

    #     if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
    #         return False

    #     visited[i][j] = True
    #     result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or\
    #         self.existRecu(board, word, cur + 1, i - 1, j, visited) or\
    #         self.existRecu(board, word, cur + 1, i, j + 1, visited) or\
    #         self.existRecu(board, word, cur + 1, i, j - 1, visited)
    #     visited[i][j] = False

    #     return result


print(Solution().exist(board=[
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], word="AX"))
