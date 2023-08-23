# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def max_depth(root) -> int:
    return max(
        max_depth(root.left),
        max_depth(root.right) 
    ) + 1 if root else 0
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        if not root:
            return True
        right_subtree_depth = max_depth(root.right)
        left_subtree_depth = max_depth(root.left)  
        if abs(right_subtree_depth - left_subtree_depth) > 1:
            return False 
        else: 
            True
        return self.isBalanced(root.right) and self.isBalanced(root.left)  

        
