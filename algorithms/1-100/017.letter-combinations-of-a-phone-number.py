class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 人家的解法
        # if not digits:
        #     return []

        # lookup, result = ["", "", "abc", "def", "ghi",
        #                   "jkl", "mno", "pqrs", "tuv", "wxyz"], [""]

        # for digit in reversed(digits):
        #     choices = lookup[int(digit)]
        #     m, n = len(choices), len(result)
        #     result += [result[i % n] for i in range(n, n * m)]

        #     for i in range(m * n):
        #         result[i] = choices[i // n] + result[i]

        # return result

        # 我的想法
        # if not digits:
        #     return []

        # digit2chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        #                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # res = [i for i in digit2chars[digits[0]]]

        # # 遍历每一个数字
        # # m+n:m和n的不重叠的组合

        # for i in digits[1:]:
        #     res = [m + n for m in res for n in digit2chars[i]]

        # return res

        # 笨办法
        tmp = list(digits)
        ans = []
        if digits == "":
            return ans
        if len(tmp) == 1:
            if tmp[0] == "2":
                ans.append("a")
                ans.append("b")
                ans.append("c")
            if tmp[0] == "3":
                ans.append("d")
                ans.append("e")
                ans.append("f")
            if tmp[0] == "4":
                ans.append("g")
                ans.append("h")
                ans.append("i")
            if tmp[0] == "5":
                ans.append("j")
                ans.append("k")
                ans.append("l")
            if tmp[0] == "6":
                ans.append("m")
                ans.append("n")
                ans.append("o")
            if tmp[0] == "7":
                ans.append("p")
                ans.append("q")
                ans.append("r")
                ans.append("s")
            if tmp[0] == "8":
                ans.append("t")
                ans.append("u")
                ans.append("v")
            if tmp[0] == "9":
                ans.append("w")
                ans.append("x")
                ans.append("y")
                ans.append("z")
            return ans
        else:
            last = self.letterCombinations(digits[1:])
            for i in range(len(last)):
                if tmp[0] == "2":
                    ans.append("a" + last[i])
                    ans.append("b" + last[i])
                    ans.append("c" + last[i])
                if tmp[0] == "3":
                    ans.append("d" + last[i])
                    ans.append("e" + last[i])
                    ans.append("f" + last[i])
                if tmp[0] == "4":
                    ans.append("g" + last[i])
                    ans.append("h" + last[i])
                    ans.append("i" + last[i])
                if tmp[0] == "5":
                    ans.append("j" + last[i])
                    ans.append("k" + last[i])
                    ans.append("l" + last[i])
                if tmp[0] == "6":
                    ans.append("m" + last[i])
                    ans.append("n" + last[i])
                    ans.append("o" + last[i])
                if tmp[0] == "7":
                    ans.append("p" + last[i])
                    ans.append("q" + last[i])
                    ans.append("r" + last[i])
                    ans.append("s" + last[i])
                if tmp[0] == "8":
                    ans.append("t" + last[i])
                    ans.append("u" + last[i])
                    ans.append("v" + last[i])
                if tmp[0] == "9":
                    ans.append("w" + last[i])
                    ans.append("x" + last[i])
                    ans.append("y" + last[i])
                    ans.append("z" + last[i])
            return ans


print(Solution().letterCombinations('27'))
