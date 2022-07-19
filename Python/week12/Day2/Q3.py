class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root):
        stack=[]
        firstNode=True
        
        while True:
            while root:
                stack.append(root)
                root=root.left
                
            if not stack:
                break
            
            node=stack.pop()
            
            if firstNode:
                newRoot=TreeNode(node.val)
                new=newRoot
                firstNode=False
            else:
                newRoot.right=TreeNode(node.val)
                newRoot=newRoot.right
            
            root=node.right
        return new
