from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # problem where they are counted twice in case [[1,0][1,1]]
        horizontal_adjacent = 0
        last = 0
        adjacent_list = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j])
                current = grid[i][j]
                if current:
                    if current.isin(adjacent_list):
                        continue
                    else:
#                         check right and down in a function

        

if __name__ == '__main__':
    test = Solution()
    test.countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])