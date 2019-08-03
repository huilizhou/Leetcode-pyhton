# 二叉树寻路
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        """
        我们会发现一个规律，在偶数行，原索引和逆序后的索引值加在一起，
        等于该行最小索引和最大索引的值（因为每一行都是一个等差数列），
        而这个值也恰好等于该行最小索引值的3倍减去1（因为下一行开始的索引是前一行开始索引的2倍）。

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
