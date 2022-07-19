class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ptr = 0
        def recursion(root):
            if not root:
                return 0
            l = recursion(root.left)
            r = recursion(root.right)
            if l+r>self.ptr:
                self.ptr = l+r
            return 1+max(l,r)
        recursion(root)
        return self.ptr
