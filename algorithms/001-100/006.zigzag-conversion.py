# Z字形变换
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # 别人的解法，numRows==0，开始step直接加一，numRows，step直接减一，很厉害。
        # 按行排序后在join
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)

        # 找出z字形变换的规律。根据图形Z来分析，每增加一层，就会增加2个步长。即步长为总层数*2-2
        # 根据步长算出第一层的所有下标。第二层就是步长-2，2交替，第三层是步长-4，4交替。
        # if numRows == 1:
        #     return s
        # step, zigzag = 2 * numRows - 2, ''
        # for i in range(numRows):
        #     for j in range(i, len(s), step):
        #         zigzag += s[j]
        #         if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
        #             zigzag += s[j + step - 2 * i]
        # return zigzag


print(Solution().convert(s="LEETCODEISHIRING", numRows=4))
