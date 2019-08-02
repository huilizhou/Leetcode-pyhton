# ip地址无效化
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # return address.replace('.', '[.]')
        address = list(address)
        for i in range(len(address)):
            if address[i] == '.':
                address[i] = '[.]'
        address = ''.join(str(i) for i in address)
        return address


print(Solution().defangIPaddr(address="1.1.1.1"))
