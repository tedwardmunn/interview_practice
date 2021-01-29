class Solution:
    def defangIPaddr(self, address: str) -> str:

        x = address.split(".")
        a = x[0]
        a = a + '[.]'
        b = x[1]
        b = b + '[.]'
        c = x[2]
        c = c + '[.]'
        d = x[3]
        address = a + b + c + d
        print(address)
        return address

test = Solution()
test.defangIPaddr("1.1.1.1")
