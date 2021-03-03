from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # problem where they are counted twice in case [[1,0][1,1]]
        horizontal_adjacent = 0
        last = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j])
                current = grid[i][j]
                if current and last:
                    horizontal_adjacent = horizontal_adjacent + 1
                last = current
        
        if horizontal_adjacent == 1:
            horizontal_adjacent = 2
        print(f"horizontal_adjacent: {horizontal_adjacent}")

        vertical_adjacent = 0
        last = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[j][i])
                current = grid[j][i]
                if current and last:
                    vertical_adjacent = vertical_adjacent + 1
                last = current

        if vertical_adjacent == 1:
            vertical_adjacent = 2

        result = horizontal_adjacent + vertical_adjacent
        print(f"Result: {result}")
        

if __name__ == '__main__':
    test = Solution()
    test.countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])