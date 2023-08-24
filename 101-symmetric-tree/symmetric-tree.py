# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def check_vals(p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:   
            return False
        elif p.val != q.val:  
            return False 
        return (
            check_vals(p.left, q.right) and 
            check_vals(p.right, q.left)
        )
    return check_vals(q, p)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        return is_same_tree(root.right, root.left)
