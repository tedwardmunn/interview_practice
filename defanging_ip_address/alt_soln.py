class Solution:
    def defangIPaddr(self, address: str) -> str:
        result_str = '[.]'.join(address.split('.'))
        return result_str

test = Solution()
print(test.defangIPaddr("1.1.1.1"))
