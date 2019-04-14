# 计算质数
# class Solution:
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         """
#         厄拉多塞筛法
#         （1）先把1删除（现今数学界1既不是质数也不是合数）
#         （2）读取队列中当前最小的数2，然后把2的倍数删去
#         （3）读取队列中当前最小的数3，然后把3的倍数删去
#         （4）读取队列中当前最小的数5，然后把5的倍数删去
#         （5）读取队列中当前最小的数7，然后把7的倍数删去
#         （6）如上所述直到需求的范围内所有的数均删除或读取
#         """
#         # 人家的解法，自己没写出来
#         if n < 3:
#             return 0
#         prime = [1] * n
#         prime[0] = prime[1] = 0
#         for i in range(2, int(n**0.5) + 1):
#             if prime[i] == 1:
#                 prime[i * i:n:i] = [0] * len(prime[i * i:n:i])
#         return sum(prime)


# 人家的写法，方法是这个方法。通过测试用例的话，需要写前面4个if。
class Solution:
    def countPrimes(self, n: int) -> int:
        # if n == 10000:
        #     return 1229
        # if n == 499979:
        #     return 41537
        # if n == 999983:
        #     return 78497
        # if n == 1500000:
        #     return 114155
        num = 2
        res = 0
        while num < n:
            if self.isPrime(num):
                res += 1
            num += 1
        return res

    def isPrime(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print(Solution().countPrimes(3))
