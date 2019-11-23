# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# [-10,-3,0,5,9]

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        else:
            return self.parseArr(nums)

    def parseArr(self, nums):
        if len(nums) == 0:
            return None
        midpoint = len(nums) // 2
        node = TreeNode(nums[midpoint])
        node.left = self.parseArr(nums[:midpoint])
        node.right = self.parseArr(nums[midpoint + 1:])
        return node
