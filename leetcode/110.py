# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.isTreeBalanced = True

    def isBalanced(self, root):
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
            print(left_depth, right_depth)
            if abs(left_depth - right_depth) > 1:
                self.isTreeBalanced = False
            return max(left_depth, right_depth) + 1


n = TreeNode(3)
n1 = TreeNode(20)
n.left = TreeNode(9)
n.right = n1
n1.left = TreeNode(15)
n1.right = TreeNode(7)

s = Solution()
is_it = s.isBalanced(n)
print(is_it)