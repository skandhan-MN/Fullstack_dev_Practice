class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        if t1 and t2:

            newNode = TreeNode(t1.val+t2.val)
            newNode.left = self.mergeTrees(t1.left, t2.left)
            newNode.right = self.mergeTrees(t1.right, t2.right)

        elif t1:

            newNode = TreeNode(t1.val)
            newNode.left = self.mergeTrees(t1.left, None)
            newNode.right = self.mergeTrees(t1.right, None)

        else:

            newNode = TreeNode(t2.val)
            newNode.left = self.mergeTrees(None, t2.left)
            newNode.right = self.mergeTrees(None, t2.right)

        return newNode