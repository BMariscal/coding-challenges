"""
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import queue

#BFS
def checkBST(root):
    diff = 0
    q = queue.Queue()
    if root == None:
        return False

    q.put(root)
    while not q.empty():
        node = q.get()
        node_val = node.data

        if node.left != None:
            l = node.left
            l_val = l.data
            diff = abs(node_val - l_val)
            if l_val > node_val:
                return False
            q.put(l)
        if node.right != None:
            r = node.right
            r_val = r.data
            if (r_val - node_val) != diff:
                return False
            if r_val < node_val:
                return False
            q.put(r)
    return True

