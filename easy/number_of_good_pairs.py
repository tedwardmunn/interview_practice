from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    out += 1
        # print(out)
        return out

if __name__ == '__main__':
    
    test1 = Solution()
    test1.numIdenticalPairs([1,2,3,1,1,3])