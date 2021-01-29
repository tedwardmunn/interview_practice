from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_array = nums[0:n]
        y_array = nums[n:(2*n)]
        out_array = []
        for i in range(n):
            out_array.append(x_array[i])
            out_array.append(y_array[i])
        print(out_array)
        return out_array


if __name__ == '__main__':
    # https://leetcode.com/problems/shuffle-the-array/
    test1 = Solution()
    test1.shuffle(nums = [2,5,1,3,4,7], n = 3)
    # test1.groupThePeople([2,2,1,1,1,1,1])