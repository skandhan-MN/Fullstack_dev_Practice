class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if root==None:
            return True

        def is_leaf(node):
            if node.left == None and node.right==None:
                return True
            return False
        
        def get_height(node):

            if is_leaf(node):
                return 1

            left  = node.left
            right = node.right
       
            if left!=None:
                h_left  = get_height(left)
                left_val = left.val
       
                if h_left == -1:
                    return -1
   
            else:
                h_left = 0
                left_val = None
   
            if right!=None:
                h_right = get_height(right)
                right_val = right.val

                if h_right == -1:
                    return -1
 
            else:
                h_right = 0
                right_val = None

            if abs(h_left-h_right)>1:
                return -1

            return max(h_left, h_right)+1
        
        res = get_height(root)
        if res==-1:
            return False
        return True
