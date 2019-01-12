class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # 人家的解法
        res = 0
        for i in zip(*A):
            if list(i) != sorted(i):
                res += 1
        return res


print(Solution().minDeletionSize(["cba", "daf", "ghi"]))
