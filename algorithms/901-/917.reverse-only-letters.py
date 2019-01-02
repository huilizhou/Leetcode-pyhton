class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 我的解法
        S = list(S)

        i, j = 0, len(S) - 1
        while i < j:
            while i < j and not S[i].isalpha():
                i += 1
            while i < j and not S[j].isalpha():
                j -= 1

            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        return "".join(S)


print(Solution().reverseOnlyLetters("ab-cd"))
