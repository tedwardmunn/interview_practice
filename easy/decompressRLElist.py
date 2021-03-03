from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            if (i % 2 == 1):
                continue
            else:
                print(i)
                for j in range(nums[i]):
                    out.append(nums[i+1])
        return out

if __name__ == "__main__":
    test = Solution()
    print(test.decompressRLElist(nums = [1,2,3,4]))