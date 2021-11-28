from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        var = str(x)
        if var[0] == '-':
            if int(var[:0:-1]) > 2147483648:
                return 0
            else:
                return(int('-' + var[:0:-1]))
        else:
            if int(var[::-1]) > 2147483648:
                return 0
            else:
                return(int(var[::-1]))

        
        
            
        

if __name__ == '__main__':
    test = Solution()
    test.reverse(x = -123)
    # print(test.getValue(0, 2))
    