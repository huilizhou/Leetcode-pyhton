# 根据身高重建队列
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: x[1])
        people.sort(key=lambda x: x[0], reverse=True)
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans


print(Solution().reconstructQueue(
    [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
