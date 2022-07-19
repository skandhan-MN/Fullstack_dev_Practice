# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        
        stack = []
        count  = 0
        ans = -1
        while(count != k):
            while(root):
                stack.append(root)
                root = root.left            
            root = stack.pop()
            ans = root.val
            count += 1
            root = root.right
        return ans

