# 总持续时间可被60整除的歌曲
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # 暴力解法，超时
        # count = 0
        # for i in range(len(time) - 1):
        #     for j in range(i + 1, len(time)):
        #         if (time[i] + time[j]) % 60 == 0:
        #             count += 1
        # return count

        # 人家的解法
        collect = [0] * 60
        for n in time:
            collect[n % 60] += 1
        ans = collect[0] * (collect[0] - 1) // 2
        for i in range(1, 30):
            ans += collect[i] * (collect[60 - i])
        ans += collect[30] * (collect[30] - 1) // 2
        return ans


print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))
