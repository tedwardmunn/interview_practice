# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode

from sqlalchemy import null


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        print("hi")



if __name__ == '__main__':
    root = TreeNode([6,7,8,2,7,1,3,9,null,1,4,null,null,null,5])
    print(root)