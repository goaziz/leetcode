class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


obj = Solution()
address = "1.1.1.1"
print(obj.defangIPaddr(address))
