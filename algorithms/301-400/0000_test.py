# s = "loveleetcode"
# print(s.find("l"), s.rfind("l"))
# mask = 0
# mask |= 1 << (ord("c") - 97)
# print(mask)
# print(1 << (ord("c") - 97))
# print(0 | 1)
# print(~60)


# # 快排的主函数，传入参数为一个列表，左右两端的下标
# def QuickSort(list, low, high):
#     if high > low:
#         # 传入参数，通过Partitions函数，获取k下标值
#         k = Partitions(list, low, high)
#         # 递归排序列表k下标左侧的列表
#         QuickSort(list, low, k - 1)
#         # 递归排序列表k下标右侧的列表
#         QuickSort(list, k + 1, high)


# def Partitions(list, low, high):
#     left = low
#     right = high
#     # 将最左侧的值赋值给参考值k
#     k = list[low]
#     # 当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
#     while left < right:
#         # 当left对应的值小于k参考值，就一直向右移动
#         while list[left] <= k:
#             left += 1
#         # 当right对应的值大于k参考值，就一直向左移动
#         while list[right] > k:
#             right = right - 1
#         # 若移动完，二者仍未相遇则交换下标对应的值
#         if left < right:
#             list[left], list[right] = list[right], list[left]
#     # 若移动完，已经相遇，则交换right对应的值和参考值
#     list[low] = list[right]
#     list[right] = k
#     # 返回k值
#     return right


# list_demo = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
# print(list_demo)
# QuickSort(list_demo, 0, 9)
# print(list_demo)


class Solution:
    def quick_sort(self, list):
        n = len(list)

        def partitions(list, start, end):
            i = start - 1
            pivot = list[end]
            for j in range(start, end):
                if list[j] < pivot:
                    i += 1
                    list[i], list[j] = list[j], list[i]
            list[i + 1], list[end] = list[end], list[i + 1]
            return i + 1

        def q_sort(list, start, end):
            if start >= end:
                return
            p = partitions(list, start, end)
            q_sort(list, start, p - 1)
            q_sort(list, p + 1, end)

        q_sort(list, 0, n - 1)
        return list


print(Solution().quick_sort([9, 8, 11, 2, 3, 4, 7]))
