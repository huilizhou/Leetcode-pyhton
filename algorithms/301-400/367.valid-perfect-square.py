class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # x = int(num**0.5)
        # if num == x * x:
        #     return True
        # else:
        #     return False

        # # 人家的解法
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid >= num // mid:
                right = mid - 1
            else:
                left = mid + 1
        return left == num // left and num % left == 0


print(Solution().isPerfectSquare(4))
