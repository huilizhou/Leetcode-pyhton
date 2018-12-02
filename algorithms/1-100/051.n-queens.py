#  N皇后问题，回溯算法的经典运用
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(col_per_row, xy_diff, xy_sum):
            cur_row = len(col_per_row)
            if cur_row == n:
                ress.append(col_per_row)
            for col in range(n):
                if col not in col_per_row and cur_row - col not in xy_diff and cur_row + col not in xy_sum:
                    dfs(col_per_row + [col], xy_diff +
                        [cur_row - col], xy_sum + [cur_row + col])

        ress = []
        dfs([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in res]for res in ress]


print(Solution().solveNQueens(4))
