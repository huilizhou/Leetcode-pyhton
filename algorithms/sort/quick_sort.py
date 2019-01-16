# 快速排序
'''
20190116 恪穆整理

1.从数列中挑出一个元素，称为“基准”（pivot），
2.重新排序数列，所有比基准值小的元素摆放在基准前面，
所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。
在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作。
3.递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归到最底部时，数列的大小是零或一，也就是已经排序好了。
这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

'''


class Solution:
    def quick_sort(self, list):
        less = []
        pivotlist = []
        more = []
        if len(list) <= 1:
            return list
        else:
            pivot = list[0]
            for i in list:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivotlist.append(i)
        less = self.quick_sort(less)
        more = self.quick_sort(more)
        return less + pivotlist + more

# 人家的简便写法
# class Solution:
#     def quick_sort(self, arr):
#         if len(arr) < 1:
#             return arr
#         else:
#             pivot = arr[0]
#             return self.quick_sort([x for x in arr[1:] if x < pivot]) + [pivot] + self.quick_sort([x for x in arr[1:] if x >= pivot])


print(Solution().quick_sort([3, 2, 4, 1, 5, 6, 10, 8]))
