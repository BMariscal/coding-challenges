# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.bfs(root.left, root.right)

    def bfs(self, root1, root2):
        if root1 == None or root2 == None:
            return root1 == root2

        if root1.val != root2.val:
            return False

        return self.bfs(root1.left, root2.right) and self.bfs(root1.right, root2.left)
