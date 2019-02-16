# 最近的请求次数
class RecentCounter:

    def __init__(self):
        self.pinglist = []
        self.minindex = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pinglist.append(t)
        while t > self.pinglist[self.minindex] + 3000:
            self.minindex += 1
        return len(self.pinglist) - self.minindex
