#  N皇后问题，回溯算法的经典运用
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 人家的思路
        # 对于任何点(x,y)，如果我们想要新点(p,q)不共享相同的行，列或对角线。
        # 那么必须有p+q!=x+y和p-q!=x-y。
        # 前者专注消除左下右上对角线。斜对角线
        # 后者专注消除左上右下对角线。正对角线

        # - col_per_row:每行的列索引列表
        # - cur_row:我们正在收索的有效的当前列
        # - xy_diff:x-y 列表
        # - xy_sum:x+y 列表

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
