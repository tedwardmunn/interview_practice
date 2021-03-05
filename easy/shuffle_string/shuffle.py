from typing import List

class Solution:

    def recurseFind(self, s, indices, out):
        curr = len(out)
        if len(out) == len(s):
            return out
        for j in range(len(s)):
            if indices[j] == curr:
                out = out + s[j]
                return(self.recurseFind(s, indices, out))
                
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = ''
        curr = 0
        return self.recurseFind(s, indices, out)
   
    


if __name__ == "__main__":
    test = Solution()
    print(test.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))