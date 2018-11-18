class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # res = []
        # if num == 1 or num == 4:
        #     return True
        # for i in range(1, num // 2):
        #     if i * i == num:
        #         res.append(i)

        # if len(res) == 1:
        #     return True
        # else:
        #     return False

        x = int(num**0.5)
        if num == x * x:
            return True
        else:
            return False

        # # 人家的解法
        # left, right = 1, num
        # while left <= right:
        #     mid = left + (right - left) / 2
        #     if mid >= num / mid:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return left == num / left and num % left == 0


print(Solution().isPerfectSquare(2))
