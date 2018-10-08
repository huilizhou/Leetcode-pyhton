class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # 我的解法
        count = 0
        for i in range(len(J)):
            if J[i] in S:
                count += S.count(J[i])
        return count

        # 人家的解法1
        # count = 0
        # for i in S:
        #     if i in J:
        #         count += 1
        # return count


print(Solution().numJewelsInStones(J="aA", S="aAAbbbb"))
