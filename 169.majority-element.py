class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = list(set(nums))
        counts = [nums.count(e) for e in elements]
        return elements[counts.index(max(counts))]

        # 人家的解法 根据题意直接求得。我们的解法是根据一般数学推导。比题意要求更为严格
        # 测试用例的话，不出现我们意想不到的情况。符合题意的应该是人家的解法如下：
        # for v in set(nums):
        #     if nums.count(v) > len(nums) // 2:
        #         return v


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
