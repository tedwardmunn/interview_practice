from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        print(target)
        result = []
        for i in range (len(nums)):
            curr = nums [i]
            for j in range(i+1, len(nums)):
                if curr + nums[j] == target:
                    result.append(i)
                    result.append(j)
        
        print(result)
            
        

if __name__ == '__main__':
    test = Solution()
    test.twoSum(nums = [2,7,11,15],target = 9)
    # print(test.getValue(0, 2))
    