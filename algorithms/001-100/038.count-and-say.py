class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        这个数列是递归定义的： 第一个为"1"，这个数有："1"个"1"，把引号里的数都连接起来，所以第二个就是"11"; 
        "11"中有："2"个"1"，把冒号后面的引号里的数都连接起来，第三个就是"21"; 
        "21"中有："1"个"2"，"1"个"1"，把冒号后面的引号里的数都连接起来，第四个就是"1211"; 
        "1211"有："1"个"1"，"1"个"2"，"2"个"1"，把冒号后面的引号里的数都连接起来，第五个就是"111221"。 
        依此类推。
        """
    #     seq = "1"
    #     for _ in range(n - 1):
    #         seq = self.getNext(seq)
    #     return seq

    # def getNext(self, seq):
    #     i, next_seq = 0, ""
    #     while i < len(seq):
    #         cnt = 1
    #         while i < len(seq) - 1 and seq[i] == seq[i + 1]:
    #             cnt += 1
    #             i += 1
    #         next_seq += str(cnt) + seq[i]
    #         i += 1
    #     return next_seq

        # 人家的解法
        # 类似于斐波拉契数，后面的数跟前面的数有关
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        pre = '11'

        for _ in range(3, n + 1):
            res = ''  # 结果，每次报数都要初始化
            cnt = 1  # 计数变量

            length = len(pre)
            for j in range(1, length):
                if pre[j - 1] == pre[j]:
                    cnt += 1
                else:
                    # 一旦遇到不同的变量，就更新结果
                    res += str(cnt) + pre[j - 1]
                    # 重置为1
                    cnt = 1
            # 把最后一项及它的数量加上
            res += str(cnt) + pre[j]
            pre = res
        return res


print(Solution().countAndSay(4))
