from typing import List

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                print(f"i: {i} j: {j}")
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

if __name__ == '__main__':
    test = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
    print(test.getValue(0, 2))
    test.updateSubrectangle(0, 0, 3, 2, 5)
    print(test.rectangle)
    test.updateSubrectangle(3, 0, 3, 2, 10)
    print(test.rectangle)

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)