# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.arr = []
        self.parser(root)
        if self.arr == sorted(self.arr) and len(set(self.arr)) == len(self.arr):
            return True
        return False

    def parser(self, root):
        if root == None:
            return root
        else:

            self.parser(root.left)
            self.arr.append(root.val)
            self.parser(root.right)
