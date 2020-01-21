# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def parseTree(root):
            height_left = 1
            height_right = 1
            if root == None:
                return 0

            else:
                height_left += parseTree(root.left)
                height_right += parseTree(root.right)
                return max(height_left, height_right)

        height = parseTree(root)
        return height