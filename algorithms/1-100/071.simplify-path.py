# 简化路径
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # 人家的写法
        pathlis = path.split("/")
        stack = []
        for e in pathlis:
            if not e or e == ".":
                continue
            elif e == "..":
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(e)
        return "/" + "/".join(stack)


print(Solution().simplifyPath("/a//b////c/d//././/.."))
