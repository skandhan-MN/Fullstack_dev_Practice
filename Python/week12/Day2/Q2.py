
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root, sum=0):
        if not root:
            return 0
        sum = sum * 2 + root.val
        if root.left or root.right:
            return self.sumRootToLeaf(root.left, sum) + self.sumRootToLeaf(root.right, sum)
        else:
            return sum