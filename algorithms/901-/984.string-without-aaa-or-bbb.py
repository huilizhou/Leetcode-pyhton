# 不含AAA或BBB的字符串
'''
直观感觉，我们应当选择所剩最多的待写字母写入字符串中，设当前所剩最多的待写字符串
'''


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == "b"
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans.append("a")
            else:
                B -= 1
                ans.append("b")
        return "".join(ans)


print(Solution().strWithout3a3b(1, 4))
