from typing import List

class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        strn = str(n)
        prod = int(strn[0])
        sumout = int(strn[0])
        for i in range(1, len(strn)):
            sumout = sumout + int(strn[i])
            prod = prod * int(strn[i])

        Result = prod - sumout
        return Result

        
    


if __name__ == "__main__":
    test = Solution()
    print(test.subtractProductAndSum(234))