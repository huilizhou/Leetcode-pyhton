# 两句话中的不常见单词
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # 官方例程
        # count = {}
        # for word in A.split():
        #     count[word] = count.get(word, 0) + 1
        # for word in B.split():
        #     count[word] = count.get(word, 0) + 1

        # return [word for word in count if count[word] == 1]

        # 人家的想法
        res = []
        allList = A.split() + B.split()
        for word in allList:
            if allList.count(word) == 1:
                res.append(word)
        return res


print(Solution().uncommonFromSentences(
    A="this apple is sweet", B="this apple is sour"))
