# 格雷编码
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 格雷码(Gray code)是一种准权码，
        # 设格雷码最低位为n＝1，则格雷码的权的绝对值为(2^n)-1，其符号从左到右正负交替。
        # 典型格雷码是一种具有反射特性和循环特性的单步自补码，
        # 它的循环、单步特性消除了随机取数时出现重大误差的可能，它的反射、自补特性使得求反非常方便。
        # 格雷码属于可靠性编码，是一种错误最小化的编码方式。

        # 从最右边起，依次将每一位与左边一位异或（XOR）
        # 作为对应的格雷码该位的值，最左边一位不变

        return [i ^ i >> 1 for i in range(2 ** n)]


print(Solution().grayCode(4))
