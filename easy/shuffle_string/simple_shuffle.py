from typing import List

class Solution:

    def restoreString(self, s: str, indices: List[int]) -> str:
        out = ['i'] * len(s)
        for i in range(len(s)):
            out[indices[i]] = s[i]
        
        return ''.join(out)
   
    


if __name__ == "__main__":
    test = Solution()
    print(test.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))