from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        print(s)
        print(indices)
        outString = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if indices[j] == i:
                    outString = outString + s[j]
        print(outString)
        return outString
        
if __name__ == "__main__":
    test = Solution()
    test.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])