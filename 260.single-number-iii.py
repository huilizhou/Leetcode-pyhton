class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # # 我的想法，参考第137题，开辟一个字典，查找值为1的个数

        res = []
        s = {}
        for i in nums:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1

        for key, value in s.items():
            if value == 1:
                res.append(key)
        return res

        # 人家的解法。20180920没看懂
        # x_xor_y = 0
        # for i in nums:
        #     x_xor_y ^= i

        # bit = x_xor_y & ~(x_xor_y - 1)

        # x = 0
        # for i in nums:
        #     if i & bit:
        #         x ^= i

        # return [x, x ^ x_xor_y]


print(Solution().singleNumber([1, 2, 1, 2, 3, 5]))
