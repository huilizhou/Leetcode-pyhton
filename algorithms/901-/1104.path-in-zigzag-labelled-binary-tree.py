# 二叉树寻路
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        if label == 1:
            return [label]
        res = [label]
        while label > 1:
            res.append(label // 2)
            label //= 2
        res.reverse()

        for i in range(1, len(res) - 1):
            if (i + 1) % 2 != len(res) % 2:
                res[i] = (3 * (2**i)) - 1 - res[i]
        return res


print(Solution().pathInZigZagTree(14))
