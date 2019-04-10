# 救生艇
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        '''
        贪心（双指针）
        如果最重的人可以与最轻的人共用一艘船，那么就那样安排。
        否则最重的人无法与任何人配对，那么他将独自乘船。

        '''

        # 人家的解法
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i


print(Solution().numRescueBoats(people=[3, 2, 3, 4], limit=5))
