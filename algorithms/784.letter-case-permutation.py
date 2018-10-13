class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # 人家的解法
        res = [""]
        for s in S:
            if not s.isalpha():
                for i in range(len(res)):
                    res[i] += s
            else:
                for i in range(len(res)):
                    res.append(res[i] + s.upper())
                    res[i] += s.lower()
        return res


print(Solution().letterCasePermutation("a1b2"))
