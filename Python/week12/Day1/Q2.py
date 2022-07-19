# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root):
        s = 0
        def f(root):
            if root is None: return
            nonlocal s
            f(root.right)
            s = s + root.val
            root.val = s
            f(root.left)
        f(root)
        return root