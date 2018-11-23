# 三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 人家的解法，利用hashmap。很有趣
        # 分情况，即三个数相同全为0，一正一负一0，两正一负，两负一正
        nums_hash = {}
        result = []
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0, 0, 0])
        neg = list(filter(lambda x: x < 0, nums_hash))
        pos = list(filter(lambda x: x >= 0, nums_hash))

        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in nums_hash:
                    if dif in (i, j) and nums_hash[dif] >= 2:
                        result.append([i, j, dif])
                    if dif < i or dif > j:
                        result.append([i, j, dif])
        return result


# # 分情况讨论解决问题。我的想法。不如hash map
#         result = []
#         d = dict()
#         for num in nums:
#             if not num in d:
#                 d[num] = 0
#             d[num] += 1

#         pos_list = [i for i in d if i > 0]
#         neg_list = [i for i in d if i < 0]

#         # 4 三个数全为0
#         if d.get(0, 0) > 2:
#             result.append([0, 0, 0])

#         # 如果全部为负或全部为正，则返回空
#         if pos_list == [] or neg_list == []:
#             return result

#         # 1 两正一负的情况
#         for i, x in enumerate(pos_list):
#             # 1(a)情况两正同样大
#             if d[x] > 1 and -2 * x in d:
#                 result.append([x, x, -2 * x])
#             # 1(b)情况，三数均不同
#             for y in pos_list[i + 1:]:
#                 if -(x + y) in d:
#                     result.append([x, y, -(x + y)])

#         # 2 两负一正的情况
#         for i, x in enumerate(neg_list):
#             # 2(a)情况两负同样大
#             if d[x] > 1 and -2 * x in d:
#                 result.append([x, x, -2 * x])
#             if y in neg_list[i + 1:]:
#                 if -(x + y) in d:
#                     result.append([x, y, -(x + y)])

#         # 3 一正一负一0
#         if 0 in d:
#             for i in pos_list:
#                 if -i in d:
#                     result.append([-i, 0, i])

#         return result


print(Solution().threeSum([-1, -1, -3, 3, 4, 5, 3, 0, 1]))
