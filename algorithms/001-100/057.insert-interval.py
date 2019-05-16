# 插入区间
# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # 我的想法。在056题基础之上，添加新的列表之后，再进行排序
        # 算法复杂度更高，不合理
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x.start)
        # l = intervals[0].start
        # r = intervals[0].end
        # ans = []
        # for i in intervals:
        #     if r >= i.start:
        #         r = max(r, i.end)
        #     else:
        #         ans.append(Interval(l, r))
        #         l = i.start
        #         r = i.end
        # ans.append(Interval(l, r))
        # return ans

        # 人家的解法
        result = []
        i = 0
        while i < len(intervals) and newInterval.start > intervals[i].end:
            result += intervals[i],
            i += 1
        while i < len(intervals) and newInterval.end >= intervals[i].start:
            newInterval = Interval(min(newInterval.start, intervals[i].start),
                                   max(newInterval.end, intervals[i].end))
            i += 1
        result += newInterval,
        result += intervals[i:]
        return result
