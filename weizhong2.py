# nums = list(map(int, input().split(' ')))


# class Solution:
#     def car_nums(self, nums):
#         # 1辆车单独装载1种货物最多的值


#         # print(Solution().car_nums(nums))
#         # print('a', a)
# print('nums', nums)


# 阳阳画三角
# N = int(input())
N = int(input())
k = 1
while N > ((k + 1) * k // 2):
    k += 1

n = N - ((k - 1) * k) // 2
if k % 1 == 1:
    print(k + 1 - n, n)
else:
    print(n, k + 1 - n)
