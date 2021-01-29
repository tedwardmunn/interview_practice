class Solution:
    def defangIPaddr(self, address: str) -> str:

        def recDefang(x,addr, count, lenAddr):
            if x >= lenAddr:
                return addr
            char = addr[x]
            print("char")
            print(char)
            print("addr")
            print(addr)
            if char == '.':
                temp = addr
                fix = temp[:x] + '[.]' + temp[x+1:]
                count = count + 1
                addr = fix
                x = x+3
                recDefang(x,addr,count, lenAddr)
            else:
                x = x+1
                recDefang(x, addr, count, lenAddr)

        initX = 0
        initCount = 0
        lenAddr = len(address)
        # soln = Solution()
        answer = recDefang(initX,address,initCount, lenAddr)
        print(answer)
        return(answer)

test = Solution()
test.defangIPaddr("1.1.1.1")
