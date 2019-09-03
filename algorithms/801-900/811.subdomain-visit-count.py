# 子域名访问计数
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # 将出现次数和域名分开
        web = []
        for i in cpdomains:
            s = i.split(' ')
            web.append([int(s[0]), s[1]])

        # 把域名拆分为子域名
        time_dic = {}
        for i in range(len(web)):
            s = web[i][1]
            while "." in s:
                s = s[s.index('.') + 1:]
                web[i].append(s)

            # 用字典记录子域名出现的次数
            for j in range(1, len(web[i])):
                if web[i][j] not in time_dic:
                    time_dic[web[i][j]] = web[i][0]
                else:
                    time_dic[web[i][j]] += web[i][0]

        res = []
        for k, v in time_dic.items():
            res.append(str(v) + " " + k)
        return res


print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))
