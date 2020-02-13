# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # BFS

        q_control = deque()
        q_control.append(root1)
        q_exp = deque()
        q_exp.append(root2)
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        root_1 = root1
        root_2 = root2
        while q_control and q_exp:
            control_node = q_control.popleft()
            exp_node = q_exp.popleft()

            if control_node and exp_node:
                if control_node.left and exp_node.left and exp_node.right and control_node.right:
                    if control_node.left.val == exp_node.right.val and control_node.right.val == exp_node.left.val:
                        temp_r = exp_node.right
                        temp_l = exp_node.left
                        exp_node.left = temp_r
                        exp_node.right = temp_l
                if (control_node.left == None and exp_node.right == None) or (
                        control_node.right == None and exp_node.left == None):
                    temp_r = exp_node.right
                    temp_l = exp_node.left
                    exp_node.left = temp_r
                    exp_node.right = temp_l

            if control_node and exp_node and control_node.left and exp_node.left:
                if control_node.left.val != exp_node.left.val:
                    return False

            if control_node:
                q_control.append(control_node.left)
                q_control.append(control_node.right)

            if exp_node:
                q_exp.append(exp_node.left)
                q_exp.append(exp_node.right)

        if str(root_1.right) == str(root_2.right) and str(root_1.left) == str(root_2.left):
            return True

        return False
