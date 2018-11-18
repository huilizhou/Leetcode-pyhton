class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 人家的解法
        # 在遍历的过程中，将target与当前的差值作为key，当前值作为value，存入字典中
        # 在存入字典之前，先判断当前值是否就在字典的keys()中

        # keys = {}
        # for i in range(len(numbers)):
        #     if target - numbers[i] in keys:
        #         return [keys[target - numbers[i]] + 1, i + 1]
        #     if numbers[i] not in keys:
        #         keys[numbers[i]] = i

        start, end = 0, len(numbers) - 1
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return[start + 1, end + 1]


print(Solution().twoSum([0, 0, 3, 4], 0))
