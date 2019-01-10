# 独特的电子邮件的地址
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            name, domain = email.split("@")
            name = name[:name.find("+")].replace(".", "")
            email_set.add(name + "@" + domain)
        return len(email_set)


print(Solution().numUniqueEmails(["test.email+alex@leetcode.com",
                                  "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
