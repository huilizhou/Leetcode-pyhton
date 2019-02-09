class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                else:
                    if (i - 1 >= 0 and board[i - 1][j] == 'X') or \
                            (j - 1 >= 0 and board[i][j - 1] == 'X'):
                        continue
                    else:
                        res += 1
        return res


print(Solution().countBattleships(
    [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
