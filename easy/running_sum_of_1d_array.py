from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums) + 1):
            curr_sum = 0
            if i == 0:
                continue
            for j in range(i):
                curr_sum = curr_sum + nums[j]
            output.append(curr_sum)
        print(output)
        return output


if __name__ == '__main__':
    # https://leetcode.com/problems/richest-customer-wealth/
    test1 = Solution()
    test1.runningSum([1,2,3,4])