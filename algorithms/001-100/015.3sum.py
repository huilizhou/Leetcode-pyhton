# 三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 人家的解法，利用hashmap。很有趣
        # 分情况，即三个数相同全为0，一正一负一0，两正一负，两负一正
        # nums_hash = {}
        # result = []
        # for num in nums:
        #     nums_hash[num] = nums_hash.get(num, 0) + 1
        # if 0 in nums_hash and nums_hash[0] >= 3:
        #     result.append([0, 0, 0])
        # neg = list(filter(lambda x: x < 0, nums_hash))
        # pos = list(filter(lambda x: x >= 0, nums_hash))

        # print(neg, pos)
        # for i in neg:
        #     for j in pos:
        #         dif = 0 - i - j
        #         if dif in nums_hash:
        #             if dif in (i, j) and nums_hash[dif] >= 2:
        #                 result.append([i, j, dif])
        #             if dif < i or dif > j:
        #                 result.append([i, j, dif])
        # return result

        # # 我的想法.
        nums_hash = {}
        result = []

        for num in nums:
            if num not in nums_hash:
                nums_hash[num] = 0
            nums_hash[num] += 1

        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0, 0, 0])

        pos_list = [i for i in nums_hash if i >= 0]
        neg_list = [i for i in nums_hash if i < 0]

        for i in pos_list:
            for j in neg_list:
                dif = 0 - i - j
                if dif in nums_hash:
                    if dif in(i, j) and nums_hash[dif] >= 2:
                        result.append([i, j, dif])
                    if dif < j or dif > i:
                        result.append([i, j, dif])
        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
