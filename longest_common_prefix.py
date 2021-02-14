from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      """
      :type strs: List[str]
      :rtype: str
      """
      if len(strs) == 0:
         return ""
      current = strs[0]
      for i in range(1,len(strs)):
         temp = ""
         if len(current) == 0:
            break
         for j in range(len(strs[i])):
            if j<len(current) and current[j] == strs[i][j]:
               temp+=current[j]
            else:
               break
         current = temp
         print(current)
      return current

        
if __name__ == "__main__":
    test = Solution()
    test.longestCommonPrefix(strs = ["flower","flow","flight"])