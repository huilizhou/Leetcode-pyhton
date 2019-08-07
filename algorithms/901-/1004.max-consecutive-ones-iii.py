# 最大连续1的个数III
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # left, right = 0, 0
        # max_length = 0
        # zero_cnt = 0

        # for right, v in enumerate(A):
        #     if v == 0:
        #         zero_cnt += 1

        #     while zero_cnt > K:
        #         if A[left] == 0:
        #             zero_cnt -= 1
        #         left += 1
        #     max_length = max(max_length, right - left + 1)

        # max_length = max(max_length, right - left + 1)
        # return max_length

        # 人家的解法
        # res = 0
        # list0 = [i for i, a in enumerate(A) if a == 0]
        # list0.append(len(A))
        # list0.insert(0, -1)
        # if len(list0) <= K + 2:
        #     return len(A)
        # else:
        #     for end in range(K, len(list0) - 1):
        #         res = max(res, list0[end + 1] - list0[end - K] - 1)
        # return res

        '''
        使用双指针left和right指代窗口的左右边界，移动right遍历整个数组。
        维护一个变量max，每次right 移动计算一次当前的最大值。
        1.当A[right]=1时，left不变，right继续移动
        2.当A[right]=0时
            1. 0的数量在K的范围内，left不变，right继续移动
            2. 0的数量>K，
                当A[left]==0时，即left指向一个零，只需要left右移一格，即可减少一个零。
                当A[left]==1时，此时窗口内包含了K个零，需要先移动至下一个零，再右移一格才能减少一个零。
        '''
        max_length = 0
        left, right = 0, 0
        for right in range(len(A)):
            if A[right] == 0:
                if K == 0:
                    while A[left] == 1:
                        left += 1
                    left += 1
                else:
                    K -= 1
            max_length = max(max_length, right - left + 1)
        return max_length


print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
