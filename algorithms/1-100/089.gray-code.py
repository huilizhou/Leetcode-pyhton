# 格雷编码
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 从最右边起，依次将每一位与左边一位异或（XOR）
        # 作为对应的格雷码该位的值，最左边一位不变

        return [i ^ i >> 1 for i in range(2 ** n)]


print(Solution().grayCode(4))
