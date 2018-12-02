# 和051类似
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
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
        return len([["." * i + "Q" + "." * (n - i - 1) for i in res]for res in ress])


print(Solution().totalNQueens(4))
