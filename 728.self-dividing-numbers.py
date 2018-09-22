class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # 我的解法有问题
        # ret = []
        # for i in range(left, right + 1):
        #     for j in range(len(str(i))):
        #         if int(str(i)[j]) != 0:
        #             while i % int(str(i)[j]) == 0:
        #                 ret.append(i)
        # return ret

        count = [i for i in range(left, right + 1) if '0' not in str(i)]
        return [i for i in count if not any([i % int(j) for j in str(i)])]

        # res = []
        # for i in range(left,right+1):
        #     k=i
        #     flag=1
        #     while k!=0:
        #         val = k % 10
        #         if val == 0 or i % val != 0:
        #             flag=0
        #             break
        #         k//=10
        #     if(flag==1):
        #         res.append(i)
        # return res


print(Solution().selfDividingNumbers(1, 22))
