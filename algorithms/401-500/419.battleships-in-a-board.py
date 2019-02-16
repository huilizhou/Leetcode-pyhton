# 甲板上的战舰
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # 人家的想法
        # 对甲板进行一次遍历，当前位置为'X'时，检测该位置的上方和左方是否为'X'。
        # 若是，则该位置并非作为一个新战舰的头部，不予处理，否则，战舰数量加一。

        # res = 0
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == '.':
        #             continue
        #         else:
        #             if (i - 1 >= 0 and board[i - 1][j] == 'X') or \
        #                     (j - 1 >= 0 and board[i][j - 1] == 'X'):
        #                 continue
        #             else:
        #                 res += 1
        # return res

        # 我的想法
        if not board:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".") and(j == 0 or board[i][j - 1] == "."):
                    count += 1
        return count


print(Solution().countBattleships(
    [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
