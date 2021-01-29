from typing import List


class Solution:

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        best = 0
        for i in range(len(accounts)):
            amount = 0
            for j in range(len(accounts[i])):
                amount = amount + accounts[i][j]
                if amount > best:
                    best = amount
        return best


if __name__ == '__main__':
    # https://leetcode.com/problems/richest-customer-wealth/
    test1 = Solution()
    test1.maximumWealth(([[1,2,3],[3,2,1]]))
