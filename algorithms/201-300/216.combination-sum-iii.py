# 组合总和III
'''
回溯法思想：
在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根结点出发深度搜索解空间树。
当探索到某一结点时，要先判断该结点是否包含问题的解，如果包含，就从该结点出发继续探索下去，
如果该结点不包含问题的解，则逐层向其祖先结点回溯。
其实回溯法就是对隐式图的深度优先搜索算法。若用回溯法求解问题的所有解，要回溯到根，
且根结点的所有可行的子树都要已被搜索遍才结束。
而若使用回溯法求任一个解时，只要搜索到问题的一个解就可以结束。
'''


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def func(start, count, sums, nums):
            if count > k or sums > n:
                return
            if count == k and sums == n:
                result.append(nums)
                return
            for x in range(start + 1, 10):
                func(x, count + 1, sums + x, nums + [x])

        func(0, 0, 0, [])
        return result


print(Solution().combinationSum3(3, 9))
