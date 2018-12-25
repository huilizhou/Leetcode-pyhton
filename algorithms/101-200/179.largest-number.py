class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 人家的解法
        import functools

        def comp(a, b): return 1 if a + b > b + \
            a else -1 if a + b < b + a else 0
        nums = list(map(str, nums))
        nums.sort(reverse=True, key=functools.cmp_to_key(comp))
        # nums.sort(cmp=comp,reverse=True)
        return str(int("".join(nums)))


print(Solution().largestNumber([10, 2]))
