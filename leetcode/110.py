# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.isTreeBalanced = True

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return self.isTreeBalanced
        self.maximumDepth(root)
        return self.isTreeBalanced

    def maximumDepth(self, root):
        if not root:
            return 0
        else:
            left_depth = self.maximumDepth(root.left)
            right_depth = self.maximumDepth(root.right)
            if abs(left_depth - right_depth) > 1:
                self.isTreeBalanced = False
            return max(left_depth, right_depth) + 1